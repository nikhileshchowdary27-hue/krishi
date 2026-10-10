import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import calc

def test_economics_normal():
    r = calc.economics(10, 2000, 12000)
    assert r["gross"] == 20000 and r["net"] == 8000 and r["margin_pct"] == 40.0

def test_negative_and_zero_revenue():
    assert calc.economics(10, 1000, 15000)["net"] == -5000
    assert calc.economics(0, 1000, 500)["margin_pct"] is None

def test_units():
    assert calc.to_acres(40, "guntha") == 1.0
    assert abs(calc.to_acres(1, "hectare") - 2.471054) < 1e-6

def test_invalid():
    for args in [(-1, "acre"), (1, "bigha")]:
        try: calc.to_acres(*args); assert False
        except ValueError: pass

def test_net_proceeds():
    assert calc.net_proceeds(50, 2000, 3000, 500)["net"] == 96500

def test_irrigation():
    r = calc.irrigation_need(5, 1.0, 10, 20, 1)
    assert r["etc_mm"] == 50 and r["net_mm"] == 34 and r["gross_mm"] == 45.3
    assert calc.irrigation_need(2, 1.0, 5, 100, 1)["net_mm"] == 0
