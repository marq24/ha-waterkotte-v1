"""Sensor platform for Waterkotte Heatpump."""
import logging

# from homeassistant.helpers.entity import Entity, EntityCategory  # , DeviceInfo
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.typing import ConfigType, HomeAssistantType

from homeassistant.const import (
    DEVICE_CLASS_DATE,
    DEVICE_CLASS_POWER_FACTOR,
    PERCENTAGE,
    DEVICE_CLASS_PRESSURE,
    DEVICE_CLASS_TEMPERATURE,
    PRESSURE_BAR,
    TEMP_CELSIUS, DEVICE_CLASS_POWER,
    POWER_KILO_WATT,
)

from homeassistant.components.sensor import (
    SensorStateClass,
)

from custom_components.waterkotte_heatpump.mypywaterkotte.xecotouch import Ecotouch2Tag
from .entity import WaterkotteHeatpumpEntity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# Sensor types are defined as:
#   variable -> [0]title, [1] EcoTouchTag, [2]device_class, [3]units, [4]icon, [5]enabled_by_default, [6]options, [7]entity_category #pylint: disable=line-too-long
SENSOR_TYPES = {
    # status sensors
    "STATUS_HEATING": [
        "Status Heating",
        Ecotouch2Tag.STATUS_HEATING,
        None,
        None,
        "mdi:sun-thermometer",
        True,
        None,
        None,
    ],
    "STATUS_WATER": [
        "Status Water",
        Ecotouch2Tag.STATUS_WATER,
        None,
        None,
        "mdi:thermometer-water",
        True,
        None,
        None,
    ],
    "STATUS_COOLING": [
        "Status Cooling",
        Ecotouch2Tag.STATUS_COOLING,
        None,
        None,
        "mdi:coolant-temperature",
        True,
        None,
        None,
    ],
    # temperature sensors
    "TEMPERATURE_OUTSIDE": [
        "Temperature Outside",
        Ecotouch2Tag.TEMPERATURE_OUTSIDE,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_OUTSIDE_1H": [
        "Temperature Outside 1h",
        Ecotouch2Tag.TEMPERATURE_OUTSIDE_1H,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_OUTSIDE_24H": [
        "Temperature Outside 24h",
        Ecotouch2Tag.TEMPERATURE_OUTSIDE_24H,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_SOURCE_ENTRY": [
        "Temperature Source Entry",
        Ecotouch2Tag.TEMPERATURE_SOURCE_ENTRY,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_SOURCE_EXIT": [
        "Temperature Source Exit",
        Ecotouch2Tag.TEMPERATURE_SOURCE_EXIT,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_EVAPORATION": [
        "Temperature Evaporation",
        Ecotouch2Tag.TEMPERATURE_EVAPORATION,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_SUCTION_LINE": [
        "Temperature Suction Line",
        Ecotouch2Tag.TEMPERATURE_SUCTION_LINE,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_RETURN_SET": [
        "Temperature Return Setpoint",
        Ecotouch2Tag.TEMPERATURE_RETURN_SET,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_RETURN": [
        "Temperature Return",
        Ecotouch2Tag.TEMPERATURE_RETURN,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_FLOW": [
        "Temperature Flow",
        Ecotouch2Tag.TEMPERATURE_FLOW,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_CONDENSATION": [
        "Temperature Condensation",
        Ecotouch2Tag.TEMPERATURE_CONDENSATION,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_BUFFERTANK": [
        "Temperature Buffer Tank",
        Ecotouch2Tag.TEMPERATURE_BUFFERTANK,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_ROOM": [
        "Temperature Room",
        Ecotouch2Tag.TEMPERATURE_ROOM,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    "TEMPERATURE_ROOM_1H": [
        "Temperature Room 1h",
        Ecotouch2Tag.TEMPERATURE_ROOM_1H,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    "TEMPERATURE_HEATING": [
        "Temperature Heating",
        Ecotouch2Tag.TEMPERATURE_HEATING,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:home-thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_HEATING_SET": [
        "Demanded Temperature Heating",
        Ecotouch2Tag.TEMPERATURE_HEATING_SET,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:home-thermometer",
        True,
        None,
        None,
    ],
    "TEMPERATURE_COOLING": [
        "Temperature Cooling",
        Ecotouch2Tag.TEMPERATURE_COOLING,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:snowflake-thermometer",
        False,
        None,
        None,
    ],
    "TEMPERATURE_COOLING_SET": [
        "Demanded Temperature Cooling",
        Ecotouch2Tag.TEMPERATURE_COOLING_SET,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:snowflake-thermometer",
        False,
        None,
        None,
    ],
    "TEMPERATURE_WATER": [
        "Temperature Hot Water",
        Ecotouch2Tag.TEMPERATURE_WATER,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer-water",
        True,
        None,
        None,
    ],
    "TEMPERATURE_WATER_SET": [
        "Demanded Temperature Hot Water",
        Ecotouch2Tag.TEMPERATURE_WATER_SET,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer-water",
        True,
        None,
        None,
    ],
    "TEMPERATURE_MIX1": [
        "Temperature mixing circle 1",
        Ecotouch2Tag.TEMPERATURE_MIX1,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer-water",
        True,
        None,
        None,
    ],
    "TEMPERATURE_MIX1_PERCENT": [
        "Temperature mixing circle 1 percent",
        Ecotouch2Tag.TEMPERATURE_MIX1_PERCENT,
        None,
        PERCENTAGE,
        "mdi:gauge",
        False,
        None,
        None,
    ],
    "TEMPERATURE_MIX1_SET": [
        "Demanded Temperature mixing circle 1",
        Ecotouch2Tag.TEMPERATURE_MIX1_SET,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer-water",
        True,
        None,
        None,
    ],
    "TEMPERATURE_MIX2": [
        "Temperature mixing circle 2",
        Ecotouch2Tag.TEMPERATURE_MIX2,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer-water",
        False,
        None,
        None,
    ],
    "TEMPERATURE_MIX2_PERCENT": [
        "Temperature mixing circle 2 percent",
        Ecotouch2Tag.TEMPERATURE_MIX2_PERCENT,
        None,
        PERCENTAGE,
        "mdi:gauge",
        False,
        None,
        None,
    ],
    "TEMPERATURE_MIX2_SET": [
        "Demanded Temperature mixing circle 2",
        Ecotouch2Tag.TEMPERATURE_MIX2_SET,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer-water",
        False,
        None,
        None,
    ],
    "TEMPERATURE_MIX3": [
        "Temperature mixing circle 3",
        Ecotouch2Tag.TEMPERATURE_MIX3,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer-water",
        False,
        None,
        None,
    ],
    "TEMPERATURE_MIX3_PERCENT": [
        "Temperature mixing circle 3 percent",
        Ecotouch2Tag.TEMPERATURE_MIX3_PERCENT,
        None,
        PERCENTAGE,
        "mdi:gauge",
        False,
        None,
        None,
    ],
    "TEMPERATURE_MIX3_SET": [
        "Demanded Temperature mixing circle 3",
        Ecotouch2Tag.TEMPERATURE_MIX3_SET,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer-water",
        False,
        None,
        None,
    ],
    "TEMPERATURE_POOL": [
        "Temperature Pool",
        Ecotouch2Tag.TEMPERATURE_POOL,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:pool-thermometer",
        False,
        None,
        None,
    ],
    "TEMPERATURE_POOL_SET": [
        "Demanded Temperature Pool",
        Ecotouch2Tag.TEMPERATURE_POOL_SET,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:pool-thermometer",
        False,
        None,
        None,
    ],
    "TEMPERATURE_SOLAR": [
        "Temperature Solar",
        Ecotouch2Tag.TEMPERATURE_SOLAR,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    "TEMPERATURE_SOLAR_EXIT": [
        "Temperature Solar Collector Exit",
        Ecotouch2Tag.TEMPERATURE_SOLAR_EXIT,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # other (none temperature) values...
    "PRESSURE_EVAPORATION": [
        "Pressure Evaporation",
        Ecotouch2Tag.PRESSURE_EVAPORATION,
        DEVICE_CLASS_PRESSURE,
        PRESSURE_BAR,
        "mdi:gauge",
        False,
        None,
        None,
    ],
    "PRESSURE_CONDENSATION": [
        "Pressure Condensation",
        Ecotouch2Tag.PRESSURE_CONDENSATION,
        DEVICE_CLASS_PRESSURE,
        PRESSURE_BAR,
        "mdi:gauge",
        False,
        None,
        None,
    ],
    # other data...
    "POSITION_EXPANSION_VALVE": [
        "Position Expansion Valve",
        Ecotouch2Tag.POSITION_EXPANSION_VALVE,
        None,
        None,
        "mdi:gauge",
        False,
        None,
        None,
    ],
    "SUCTION_GAS_OVERHEATING": [
        "Suction Gas Overheating",
        Ecotouch2Tag.SUCTION_GAS_OVERHEATING,
        None,
        None,
        "mdi:gauge",
        False,
        None,
        None,
    ],
    "POWER_ELECTRIC": [
        "Power Electrical",
        Ecotouch2Tag.POWER_ELECTRIC,
        DEVICE_CLASS_POWER,
        POWER_KILO_WATT,
        "mdi:lightning-bolt",
        True,
        None,
        None,
    ],
    "POWER_HEATING": [
        "Power Thermal",
        Ecotouch2Tag.POWER_HEATING,
        DEVICE_CLASS_POWER,
        POWER_KILO_WATT,
        "mdi:lightning-bolt",
        True,
        None,
        None,
    ],
    "POWER_COOLING": [
        "Power Cooling",
        Ecotouch2Tag.POWER_COOLING,
        DEVICE_CLASS_POWER,
        POWER_KILO_WATT,
        "mdi:lightning-bolt",
        True,
        None,
        None,
    ],
    "COP_HEATING": [
        "COP Heating",
        Ecotouch2Tag.COP_HEATING,
        None,
        SensorStateClass.MEASUREMENT,
        "mdi:gauge",
        True,
        None,
        None,
    ],
    "COP_COOLING": [
        "COP Cooling",
        Ecotouch2Tag.COP_COOLING,
        None,
        SensorStateClass.MEASUREMENT,
        "mdi:gauge",
        True,
        None,
        None,
    ],
    "PERCENT_HEAT_CIRC_PUMP": [
        "Percent Heat Circ Pump",
        Ecotouch2Tag.PERCENT_HEAT_CIRC_PUMP,
        DEVICE_CLASS_POWER_FACTOR,
        PERCENTAGE,
        "mdi:gauge",
        False,
        None,
        None,
    ],
    "PERCENT_SOURCE_PUMP": [
        "Percent Source Pump",
        Ecotouch2Tag.PERCENT_SOURCE_PUMP,
        DEVICE_CLASS_POWER_FACTOR,
        PERCENTAGE,
        "mdi:gauge",
        False,
        None,
        None,
    ],
    "PERCENT_COMPRESSOR": [
        "Percent Compressor",
        Ecotouch2Tag.PERCENT_COMPRESSOR,
        DEVICE_CLASS_POWER_FACTOR,
        PERCENTAGE,
        "mdi:gauge",
        False,
        None,
        None,
    ],
    # writeable sensors from here...
    "HOLIDAY_START_TIME": [
        "Holiday start",
        Ecotouch2Tag.HOLIDAY_START_TIME,
        DEVICE_CLASS_DATE,
        None,
        "mdi:calendar-arrow-right",
        True,
        None,
        None,
    ],
    "HOLIDAY_END_TIME": [
        "Holiday end",
        Ecotouch2Tag.HOLIDAY_END_TIME,
        DEVICE_CLASS_DATE,
        None,
        "mdi:calendar-arrow-left",
        True,
        None,
        None,
    ],
    "STATE_SERVICE": [
        "State Service",
        Ecotouch2Tag.STATE_SERVICE,
        None,
        None,
        None,
        True,
        None,
        None,
    ],
    # Kuehlung...
    # A109
    "TEMPERATURE_COOLING_SETPOINT": [
        "Temperature Cooling Demand",
        Ecotouch2Tag.TEMPERATURE_COOLING_SETPOINT,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # A108
    "TEMPERATURE_COOLING_OUTDOOR_LIMIT": [
        "Temperature Cooling Outdoor Limit",
        Ecotouch2Tag.TEMPERATURE_COOLING_OUTDOOR_LIMIT,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],

    # We should not use the HEATING setpoint directly - adjust
    # the heat curve instead!
    #"temp_heating_setpoint": [
    #    "Temperature Heating Demand",
    #    EcotouchTag.TEMPERATURE_HEATING_SETPOINT,
    #    DEVICE_CLASS_TEMPERATURE,
    #    TEMP_CELSIUS,
    #    "mdi:thermometer",
    #    False,
    #    None,
    #    None,
    #],

    # Heizung - Heizkennlinie
    # A93
    "TEMPERATURE_HEATING_HC_LIMIT": [
        "Temperature heating curve heating limit",
        Ecotouch2Tag.TEMPERATURE_HEATING_HC_LIMIT,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # A94
    "TEMPERATURE_HEATING_HC_TARGET": [
        "Temperature heating curve heating limit target",
        Ecotouch2Tag.TEMPERATURE_HEATING_HC_TARGET,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # A91
    "TEMPERATURE_HEATING_HC_OUTDOOR_NORM": [
        "Temperature heating curve norm outdoor",
        Ecotouch2Tag.TEMPERATURE_HEATING_HC_OUTDOOR_NORM,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # A92
    "TEMPERATURE_HEATING_HC_NORM": [
        "Temperature heating curve norm heating circle",
        Ecotouch2Tag.TEMPERATURE_HEATING_HC_NORM,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # A95
    "TEMPERATURE_HEATING_SETPOINTLIMIT_MAX": [
        "Temperature heating curve Limit for setpoint (Max.)",
        Ecotouch2Tag.TEMPERATURE_HEATING_SETPOINTLIMIT_MAX,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # A104
    "TEMPERATURE_HEATING_SETPOINTLIMIT_MIN": [
        "Temperature heating curve Limit for setpoint (Min.)",
        Ecotouch2Tag.TEMPERATURE_HEATING_SETPOINTLIMIT_MIN,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # A38 - Warmwasser
    "TEMPERATURE_WATER_SETPOINT": [
        "Temperature Hot Water setpoint",
        Ecotouch2Tag.TEMPERATURE_WATER_SETPOINT,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # Mischerkreis 1 Heizkennlinie
    # A276
    "TEMPERATURE_MIX1_HC_LIMIT": [
        "Temperature mixing circle 1 heating limit",
        Ecotouch2Tag.TEMPERATURE_MIX1_HC_LIMIT,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # A277
    "TEMPERATURE_MIX1_HC_TARGET": [
        "Temperature mixing circle 1 heating limit target",
        Ecotouch2Tag.TEMPERATURE_MIX1_HC_TARGET,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # A274
    "TEMPERATURE_MIX1_HC_OUTDOOR_NORM": [
        "Temperature mixing circle 1 norm outdoor",
        Ecotouch2Tag.TEMPERATURE_MIX1_HC_OUTDOOR_NORM,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # A275
    "TEMPERATURE_MIX1_HC_HEATING_NORM": [
        "Temperature mixing circle 1 norm heating circle",
        Ecotouch2Tag.TEMPERATURE_MIX1_HC_HEATING_NORM,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # A278
    "TEMPERATURE_MIX1_HC_MAX": [
        "Temperature mixing circle 1 Limit for setpoint (Max.)",
        Ecotouch2Tag.TEMPERATURE_MIX1_HC_MAX,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    # Mischerkreis 2 Heizkennlinie
    "TEMPERATURE_MIX2_HC_LIMIT": [
        "Temperature mixing circle 2 heating limit",
        Ecotouch2Tag.TEMPERATURE_MIX2_HC_LIMIT,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    "TEMPERATURE_MIX2_HC_TARGET": [
        "Temperature mixing circle 2 heating limit target",
        Ecotouch2Tag.TEMPERATURE_MIX2_HC_TARGET,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    "TEMPERATURE_MIX2_HC_OUTDOOR_NORM": [
        "Temperature mixing circle 2 norm outdoor",
        Ecotouch2Tag.TEMPERATURE_MIX2_HC_OUTDOOR_NORM,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    "TEMPERATURE_MIX2_HC_HEATING_NORM": [
        "Temperature mixing circle 2 norm heating circle",
        Ecotouch2Tag.TEMPERATURE_MIX2_HC_HEATING_NORM,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
    "TEMPERATURE_MIX2_HC_MAX": [
        "Temperature mixing circle 2 Limit for setpoint (Max.)",
        Ecotouch2Tag.TEMPERATURE_MIX2_HC_MAX,
        DEVICE_CLASS_TEMPERATURE,
        TEMP_CELSIUS,
        "mdi:thermometer",
        False,
        None,
        None,
    ],
}

# async def async_setup_entry(hass: HomeAssistantType, entry: ConfigType, async_add_entities) -> None:
async def async_setup_entry(
    hass: HomeAssistantType, entry: ConfigType, async_add_devices
) -> None:
    """Set up the Waterkotte sensor platform."""

    _LOGGER.debug("Sensor async_setup_entry")
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        [
            WaterkotteHeatpumpSensor(entry, coordinator, sensor_type)
            for sensor_type in SENSOR_TYPES
        ]
    )


class WaterkotteHeatpumpSensor(SensorEntity, WaterkotteHeatpumpEntity):
    """waterkotte_heatpump Sensor class."""

    def __init__(
        self, entry, hass_data, sensor_type
    ):  # pylint: disable=unused-argument
        """Initialize the sensor."""
        # super().__init__(self, hass_data)
        self._coordinator = hass_data

        self._type = sensor_type
        self._name = f"{SENSOR_TYPES[self._type][0]}"
        self._unique_id = self._type
        self._entry_data = entry.data
        self._device_id = entry.entry_id
        hass_data.alltags.update({self._unique_id: SENSOR_TYPES[self._type][1]})
        super().__init__(hass_data, entry)

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def tag(self):
        """Return a unique ID to use for this entity."""
        return SENSOR_TYPES[self._type][1]

    @property
    def state(self):
        """Return the state of the sensor."""
        # result = ""
        # print(self._coordinator.data)
        try:
            sensor = SENSOR_TYPES[self._type]
            value = self._coordinator.data[sensor[1]]["value"]
            if value is None or value == "":
                value = "unknown"
        except KeyError:
            value = "unknown"
        except TypeError:
            return "unknown"
        if value is True:
            value = "on"
        elif value is False:
            value = "off"
        return value

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return SENSOR_TYPES[self._type][4]
        # return ICON

    @property
    def device_class(self):
        """Return the device class of the sensor."""
        return SENSOR_TYPES[self._type][2]

    @property
    def entity_registry_enabled_default(self):
        """Return the entity_registry_enabled_default of the sensor."""
        return SENSOR_TYPES[self._type][5]

    @property
    def entity_category(self):
        """Return the unit of measurement."""
        return SENSOR_TYPES[self._type][7]

    @property
    def unique_id(self):
        """Return the unique of the sensor."""
        return self._unique_id

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return SENSOR_TYPES[self._type][3]

    async def async_update(self):
        """Schedule a custom update via the common entity update service."""
        await self._coordinator.async_request_refresh()

    @property
    def should_poll(self) -> bool:
        """Entities do not individually poll."""
        return False
