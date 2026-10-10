from pathlib import Path
from typing import List
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from . import calc

app = FastAPI(title="KrishiMitra AI", version="0.1.0")
Unit = str

class Crop(BaseModel):
    name: str = Field(min_length=1, max_length=60)
    yield_per_acre: float = Field(ge=0)   # quintal/acre (user assumption)
    price: float = Field(ge=0)            # Rs/quintal (user assumption)
    cost_per_acre: float = Field(ge=0)    # Rs/acre (user assumption)

class ScenarioReq(BaseModel):
    area: float = Field(gt=0); unit: Unit = "acre"
    crops: List[Crop] = Field(min_length=1, max_length=6)
    yield_adj: float = Field(1.0, ge=0.1, le=3); price_adj: float = Field(1.0, ge=0.1, le=3)

class Market(BaseModel):
    name: str = Field(min_length=1, max_length=60)
    price: float = Field(ge=0); transport: float = Field(0, ge=0)

class MarketReq(BaseModel):
    quantity: float = Field(gt=0); other_costs: float = Field(0, ge=0)
    markets: List[Market] = Field(min_length=1, max_length=10)

class IrrigReq(BaseModel):
    et0: float = Field(ge=0); kc: float = Field(ge=0, le=2)
    days: int = Field(ge=1, le=60); rain_mm: float = Field(0, ge=0)
    area: float = Field(gt=0); unit: Unit = "acre"

def acres(v, u):
    try: return calc.to_acres(v, u)
    except ValueError as e:
        from fastapi import HTTPException; raise HTTPException(422, str(e))

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/api/v1/scenarios/compare")
def compare(r: ScenarioReq):
    a = acres(r.area, r.unit)
    return {"calc_version": calc.CALC_VERSION, "data_origin": "user-provided assumptions",
            "results": [{"name": c.name, "scenarios": calc.crop_scenarios(
                a, c.yield_per_acre, c.price, c.cost_per_acre, r.yield_adj, r.price_adj)} for c in r.crops]}

@app.post("/api/v1/markets/compare")
def markets(r: MarketReq):
    rows = [{"name": m.name, "price": m.price, "transport": m.transport,
             **calc.net_proceeds(r.quantity, m.price, m.transport, r.other_costs),
             "source": "user-provided", "observed_at": None} for m in r.markets]
    return {"results": sorted(rows, key=lambda x: -x["net"])}

@app.post("/api/v1/irrigation/plan")
def irrigation(r: IrrigReq):
    res = calc.irrigation_need(r.et0, r.kc, r.days, r.rain_mm, acres(r.area, r.unit))
    return {**res, "method": "FAO-56 style approximation from user-provided inputs"}

app.mount("/", StaticFiles(directory=Path(__file__).resolve().parents[2] / "frontend", html=True), name="web")
