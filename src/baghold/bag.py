# Copyright 2026 Digital Currensy Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Score a pit mouth from the numbers the caller supplies. This does not survey a cave."""


import math


def _bad(value: float | None) -> bool:
    return value is not None and not math.isfinite(value)


def hold(
    mouth_m: float | None,
    floor_void_fraction: float | None,
    drop_m: float | None,
    floor_slope_deg: float | None,
) -> str:
    """Missing mouth, void fraction, or floor slope is not a pass.

    Order: missing required input, a negative measure or a void fraction
    outside 0 to 1, then pinch, voids, drop, slope, else ok.
    A missing drop is not required and is not a fail by itself.
    A negative drop is missing.
    """
    if mouth_m is None or floor_void_fraction is None or floor_slope_deg is None:
        return "missing"
    if _bad(mouth_m) or _bad(floor_void_fraction) or _bad(drop_m) or _bad(floor_slope_deg):
        return "missing"
    if (
        mouth_m < 0
        or floor_void_fraction < 0
        or floor_void_fraction > 1
        or floor_slope_deg < 0
    ):
        return "missing"
    if drop_m is not None and drop_m < 0:
        return "missing"
    if mouth_m < 30:
        return "pinch"
    if floor_void_fraction > 0.15:
        return "voids"
    if drop_m is not None and drop_m > 30:
        return "drop"
    if floor_slope_deg > 20:
        return "slope"
    return "ok"

