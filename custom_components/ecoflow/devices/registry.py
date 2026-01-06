from collections import OrderedDict
from typing import Type

from custom_components.ecoflow.devices import BaseDevice, DiagnosticDevice

from custom_components.ecoflow.devices.internal import (
    delta_3_max_plus as internal_delta_3_max_plus,
)
from custom_components.ecoflow.devices.public import (
    delta_3_max_plus as public_delta_3_max_plus,
)

devices: OrderedDict[str, Type[BaseDevice]] = OrderedDict[str, Type[BaseDevice]](
    {
        "DELTA_3_MAX_PLUS": internal_delta_3_max_plus.Delta3MaxPlus,
    }
)

device_by_product: OrderedDict[str, Type[BaseDevice]] = OrderedDict[str, Type[BaseDevice]](
    {
        "DELTA 3 Max Plus": public_delta_3_max_plus.Delta3MaxPlus,
    }
)
