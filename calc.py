"""Deterministic calculations (calc version 1.0). No AI is used here."""
CALC_VERSION = "1.0"
AREA_TO_ACRE = {"acre": 1.0, "hectare": 2.471054, "guntha": 0.025, "cent": 0.01}
ACRE_M2 = 4046.856

def to_acres(value: float, unit: str) -> float:
    if unit not in AREA_TO_ACRE:
        raise ValueError(f"unsupported unit: {unit}")
    if value < 0:
        raise ValueError("area must be >= 0")
    return value * AREA_TO_ACRE[unit]

def economics(harvest_qty, price, total_cost):
    gross = harvest_qty * price
    net = gross - total_cost
    margin = (net / gross * 100) if gross > 0 else None  # undefined when no revenue
    return {"gross": round(gross, 2), "cost": round(total_cost, 2),
            "net": round(net, 2), "margin_pct": None if margin is None else round(margin, 1)}

# Illustrative planning assumptions, NOT statistically calibrated predictions.
CASES = {"low": (0.85, 0.90), "reference": (1.0, 1.0), "high": (1.15, 1.10)}

def crop_scenarios(area_acres, yield_per_acre, price, cost_per_acre, yield_adj=1.0, price_adj=1.0):
    out = {}
    for name, (yf, pf) in CASES.items():
        qty = area_acres * yield_per_acre * yf * yield_adj
        out[name] = economics(qty, price * pf * price_adj, area_acres * cost_per_acre)
    return out

def net_proceeds(qty, price, transport, other):
    gross = qty * price
    return {"gross": round(gross, 2), "net": round(gross - transport - other, 2)}

def irrigation_need(et0_mm_day, kc, days, rain_mm, area_acres, rain_eff=0.8, app_eff=0.75):
    """FAO-56 style approximation: ETc = ET0*Kc; need = (ETc*days - effective rain)/efficiency."""
    etc = et0_mm_day * kc * days
    net_mm = max(0.0, etc - rain_mm * rain_eff)
    gross_mm = net_mm / app_eff
    return {"etc_mm": round(etc, 1), "net_mm": round(net_mm, 1), "gross_mm": round(gross_mm, 1),
            "litres": round(gross_mm * area_acres * ACRE_M2)}  # 1 mm over 1 m2 = 1 L
