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

"""Two published bags. Declared hold stats. Not a scored hold."""

MTP = {
    "id": "BAG-MTP-TRANQ",
    "name": "Mare Tranquillitatis pit",
    "lat": 8.336,
    "lon": 33.222,
    "alt": (8.3, 33.2),
    "mouth_m": 88,
    "mouth_max_m": 100,
    "drop_m": 133,
    "floor_void_fraction": 0.40,
    "floor_slope_deg": 15,
    "overhang_m": 20,
    "west_void_m": 40,
    "fetched": False,
}

MHP = {
    "id": "BAG-MHP-MARIUS",
    "name": "Marius Hills pit",
    "lat": 14.091,
    "lon": 303.230,
    "alt": (14.2, 303.3),
    "mouth_m": 49,
    "mouth_max_m": 55,
    "drop_m": 60,
    "floor_void_fraction": 0.08,
    "floor_slope_deg": 5,
    "overhang_m": 12,
    "dtm": "NAC_DTM_MARIUSPIT01",
    "fetched": False,
}

INGENII = {
    "id": "ingenii",
    "name": "Mare Ingenii pit",
    "lat": -35.948,
    "lon": 166.053,
    "this_catalog": False,
}

LACUS_MORTIS = {
    "id": "lacus-mortis",
    "name": "Lacus Mortis pit",
    "lat": 44.962,
    "lon": 25.610,
    "this_catalog": False,
}
