# Market-SII Runbook

## Local Development

### Backend

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Docker

```bash
docker compose up --build
```

## Real Market Data Smoke Test

Run the full structural intelligence pipeline against live Yahoo Finance market data:

```bash
python scripts/run_real_data_smoke.py
```

Outputs:

```text
outputs/real_market_sii_snapshot.json
```

## Primary Endpoints

- GET /snapshot/current
- GET /snapshot/health-score
- GET /regime
- GET /replay/timeline
- WS /stream/market-state

## Environment Variables

See:
- .env.example
- frontend/.env.local.example
