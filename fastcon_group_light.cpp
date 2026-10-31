#include "fastcon_group_light.h"
#include "esphome/core/log.h"

namespace esphome {
namespace fastcon_group_light {

static const char *const TAG = "fastcon_group_light";

void FastconGroupLight::write_state(light::LightState *state) {
  if (this->controller_ == nullptr) {
    ESP_LOGE(TAG, "No controller set");
    return;
  }

  auto values = state->current_values;
  bool is_on = values.is_on();

  // Exact payloads captured from brMesh app for group on/off
  // ON:  43 2a a8 00 80 00 00 00 00 00 00 00
  // OFF: 43 2a a8 00 00 00 00 00 00 00 00 00
  std::vector<uint8_t> payload = {0x43, 0x2a, 0xa8, 0x00,
                                  is_on ? 0x80 : 0x00,
                                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};

  // TODO: send group selector first if needed, then this payload
  // For now this uses the same advertising path as single lights
  this->controller_->single_control(0xFD, payload);  // 0xFD is the group address seen in captures

  ESP_LOGD(TAG, "Sent group %s command", is_on ? "ON" : "OFF");
}

}  // namespace fastcon_group_light
}  // namespace esphome
