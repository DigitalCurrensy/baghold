"""One bad bag. Mare Tranquillitatis pit walked. Marius Hills named, not this walk."""

from __future__ import annotations

import math

from .bag import hold
from .bags import MHP, MTP

MOON_RADIUS_M = 1_737_400

MTP_WALK = {
    "id": "BAG-MTP-TRANQ",
    "lat": 8.336,
    "lon": 33.222,
    "frame": "planetocentric ME/PA Wagner and Robinson 2022",
    "haruyama": (8.3, 33.2),
    "carrer": (8.3355, 33.222),
    "haruyama_m": 1276,
    "carrer_m": 15,
    "west_void_m": 40,
    "overhang_m": 20,
    "lola_gap_m": 500,
    "mouth_m": 88,
}


def lunar_offset_m(a: tuple[float, float], b: tuple[float, float]) -> float:
    to_r = math.pi / 180.0
    p1, p2 = a[0] * to_r, b[0] * to_r
    dp = (b[0] - a[0]) * to_r
    dl = (b[1] - a[1]) * to_r
    s = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * MOON_RADIUS_M * math.asin(min(1.0, math.sqrt(s)))


def score_published() -> str:
    return hold(MTP["mouth_m"], MTP["floor_void_fraction"], MTP["drop_m"], MTP["floor_slope_deg"])


def score_mhp() -> str:
    return hold(MHP["mouth_m"], MHP["floor_void_fraction"], MHP["drop_m"], MHP["floor_slope_deg"])
