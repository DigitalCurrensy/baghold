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

def hold(
    mouth_m: float,
    floor_void_fraction: float,
    drop_m: float | None,
    floor_slope_deg: float,
) -> str:
    if mouth_m < 30:
        return "pinch"
    if floor_void_fraction > 0.15:
        return "voids"
    if drop_m is not None and drop_m > 30:
        return "drop"
    if floor_slope_deg > 20:
        return "slope"
    return "ok"
