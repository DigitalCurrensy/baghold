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
