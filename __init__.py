import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import light
from esphome.const import CONF_ID
from ..fastcon import FastconController

DEPENDENCIES = ["fastcon"]

fastcon_group_light_ns = cg.esphome_ns.namespace("fastcon_group_light")
FastconGroupLight = fastcon_group_light_ns.class_("FastconGroupLight", light.LightOutput, cg.Component)

CONFIG_SCHEMA = light.LIGHT_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(FastconGroupLight),
        cv.Required("controller_id"): cv.use_id(FastconController),
        cv.Required("start_light_id"): cv.int_range(min=1, max=255),
        cv.Required("mask"): cv.hex_int_range(min=1, max=255),
    }
).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await light.register_light(var, config)

    controller = await cg.get_variable(config["controller_id"])
    cg.add(var.set_controller(controller))
    cg.add(var.set_start_light_id(config["start_light_id"]))
    cg.add(var.set_mask(config["mask"]))
