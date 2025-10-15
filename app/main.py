from fastapi import FastAPI, HTTPException
from time import time
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import PlainTextResponse
import numpy as np

from .schemas import ScoreRequest, ScoreResponse
from .features import featurize
from .model import model_service
from .logger import get_logger

app = FastAPI(title="Capgemini Real-Time ML Platform", version="1.0.0")
log = get_logger()

REQUESTS = Counter("api_requests_total", "Total API requests", ["route", "method", "code"])
LAT = Histogram("api_request_latency_seconds", "Latency per route", ["route", "method"])

@app.get("/health")
def health():
    REQUESTS.labels("/health","GET","200").inc()
    return {"status": "ok", "model_trained_at": model_service.meta.get("trained_at")}

@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.post("/score", response_model=ScoreResponse)
def score(req: ScoreRequest):
    start = time()
    try:
        feats = featurize(req.features)
        p = model_service.predict_proba(np.array(feats))
        resp = ScoreResponse(score=p, model_auc=model_service.meta.get("auc", 0.0), model_trained_at=model_service.meta.get("trained_at",""))
        REQUESTS.labels("/score","POST","200").inc()
        return resp
    except Exception as e:
        log.exception("scoring_failed")
        REQUESTS.labels("/score","POST","500").inc()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        LAT.labels("/score","POST").observe(time() - start)
