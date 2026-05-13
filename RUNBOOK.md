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
