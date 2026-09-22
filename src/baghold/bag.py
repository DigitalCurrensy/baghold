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
