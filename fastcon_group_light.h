#pragma once

#include "esphome/core/component.h"
#include "esphome/components/light/light_output.h"
#include "esphome/components/fastcon/fastcon_controller.h"

namespace esphome {
namespace fastcon_group_light {

class FastconGroupLight : public light::LightOutput, public Component {
 public:
  void set_controller(fastcon::FastconController *controller) { controller_ = controller; }
  void set_start_light_id(uint8_t id) { start_light_id_ = id; }
  void set_mask(uint8_t mask) { mask_ = mask; }

  light::LightTraits get_traits() override {
    auto traits = light::LightTraits();
    traits.set_supported_color_modes({light::ColorMode::RGB});
    return traits;
  }

  void write_state(light::LightState *state) override;

 protected:
  fastcon::FastconController *controller_{nullptr};
  uint8_t start_light_id_{1};
  uint8_t mask_{0x03};
};

}  // namespace fastcon_group_light
}  // namespace esphome
