import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import select
from . import midea_dehum_ns, CONF_MIDEA_DEHUM_ID

cg.add_define("USE_MIDEA_DEHUM_SELECT")

MideaDehum = midea_dehum_ns.class_("MideaDehumComponent", cg.Component)
MideaModeSelect = midea_dehum_ns.class_("MideaModeSelect", select.Select, cg.Component)

CONF_MODE = "mode"
MODE_OPTIONS = ["Setpoint", "Continuous", "Smart", "ClothesDrying"]

CONFIG_SCHEMA = cv.Schema({
    cv.Required(CONF_MIDEA_DEHUM_ID): cv.use_id(MideaDehum),
    cv.Optional(CONF_MODE): select.select_schema(
        MideaModeSelect,
        icon="mdi:tune-variant",
    ),
})


async def to_code(config):
    parent = await cg.get_variable(config[CONF_MIDEA_DEHUM_ID])

    if CONF_MODE in config:
        mode_select = await select.new_select(
            config[CONF_MODE],
            options=MODE_OPTIONS,
        )
        cg.add(parent.set_mode_select(mode_select))