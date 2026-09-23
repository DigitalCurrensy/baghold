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

"""BAGHOLD — the bag is the goal. Score the hold. Do not pretty-print a cave."""

from .bag import hold
from .bags import INGENII, LACUS_MORTIS, MHP, MTP
from .counsel import compile_counsel, void_edge
from .letter import compile_letter, void_fraction_of
from .walk import MTP_WALK, lunar_offset_m

__all__ = [
    "INGENII",
    "LACUS_MORTIS",
    "MHP",
    "MTP",
    "MTP_WALK",
    "compile_counsel",
    "compile_letter",
    "hold",
    "lunar_offset_m",
    "void_edge",
    "void_fraction_of",
]
