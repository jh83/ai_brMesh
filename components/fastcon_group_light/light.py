import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import light
from esphome.const import CONF_OUTPUT_ID

DEPENDENCIES = ["fastcon", "light"]
AUTO_LOAD = ["light"]

CONF_CONTROLLER_ID = "controller_id"
CONF_START_LIGHT_ID = "start_light_id"
CONF_MASK = "mask"

fastcon_ns = cg.esphome_ns.namespace("fastcon")
FastconController = fastcon_ns.class_("FastconController", cg.Component)

group_ns = cg.esphome_ns.namespace("fastcon_group_light")
FastconGroupLight = group_ns.class_("FastconGroupLight", light.LightOutput, cg.Component)

CONFIG_SCHEMA = light.RGB_LIGHT_SCHEMA.extend(
    {
        cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(FastconGroupLight),
        cv.Required(CONF_CONTROLLER_ID): cv.use_id(FastconController),
        cv.Required(CONF_START_LIGHT_ID): cv.int_range(min=1, max=255),
        cv.Required(CONF_MASK): cv.int_range(min=1, max=255),
    }
).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_OUTPUT_ID])
    await cg.register_component(var, config)
    await light.register_light(var, config)

    controller = await cg.get_variable(config[CONF_CONTROLLER_ID])
    cg.add(var.set_controller(controller))
    cg.add(var.set_start_light_id(config[CONF_START_LIGHT_ID]))
    cg.add(var.set_mask(config[CONF_MASK]))