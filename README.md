# Fastcon RGB Group Fix

Minimal custom component that sends the exact group ON/OFF payloads captured from the brMesh app.

## Usage

1. Push this folder to your GitHub repo (e.g. `youruser/esphome-fastcon-rgb-group`).

2. In your ESPHome YAML:

```yaml
external_components:
  - source: github://youruser/esphome-fastcon-rgb-group
    components: [fastcon, fastcon_group_light]

# ... your existing fastcon: controller and individual lights ...

light:
  - platform: fastcon_group_light
    name: "Both Lights"
    controller_id: fastcon_controller
    start_light_id: 1
    mask: 0x03
    default_transition_length: 0s
```

## Notes

- This currently only implements reliable ON/OFF for groups using the captured payloads:
  - ON: `43 2a a8 00 80 00 00 00 00 00 00 00`
  - OFF: `43 2a a8 00 00 00 00 00 00 00 00 00`
- Brightness and RGB color still need the full group protocol (selector + color payload).
- You still need the original `fastcon` controller component (copy it from scross01 or include it here).

Copy the `fastcon` folder from https://github.com/scross01/esphome-fastcon/tree/dev/components/fastcon into this repo's `components/` directory before pushing.
