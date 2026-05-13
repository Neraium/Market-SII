from fastapi import FastAPI

app = FastAPI(title="Market-SII")


@app.get("/")
def root():
    return {
        "system": "Market-SII",
        "status": "online",
        "description": "Systemic market structure intelligence engine",
    }


@app.get("/health")
def health():
    return {
        "health": "stable"
    }


@app.get("/regime")
def regime():
    return {
        "regime": "transition"
    }
