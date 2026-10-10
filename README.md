# KrishiMitra AI (starter)

Bilingual (English/Telugu) farming decision-support web app: crop scenario comparison, market net-proceeds comparison, and irrigation water estimate. FastAPI backend serves the API and the static frontend.

## Run locally
```
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://localhost:8000 (API docs at /docs).

## Test
```
cd backend && python -m pytest -q
```

## What is implemented
- Deterministic, unit-tested calculations (`backend/app/calc.py`): revenue, net return, margin (undefined when revenue is 0), unit conversion (acre, hectare, guntha, cent), net proceeds, FAO-56 style irrigation need.
- Three crops compared with Low / Reference / High cases; sliders recalculate live ("change my conditions").
- Market comparison from user-entered prices; irrigation estimate from user-entered ET0, Kc and rainfall.
- English/Telugu UI switch, input validation, error messages, keyboard-visible focus.

## Not implemented yet (see docs/SOP and your master prompt)
Authentication, PostgreSQL persistence and saved reports, farm profiles, the AI assistant (LLM + retrieval + voice), live AGMARKNET/weather integrations, offline caching, e2e tests, deployment. `.env.example` lists the planned variables. All default values in the UI are sample values, not agronomic recommendations or live prices.

## Deploy
Any Python host that can run `uvicorn app.main:app --host 0.0.0.0 --port $PORT` works. Verify `/health` and test from a second device before sharing the URL.
