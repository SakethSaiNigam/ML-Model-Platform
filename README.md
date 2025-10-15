# Capgemini Real-Time ML Platform (Portfolio Project)

**Author:** Saketh Sai Nigam Kanduri — Software Engineer, Capgemini

A production-style reference project showing how to serve ML predictions via a FastAPI microservice with CI/CD, containerization, Helm manifests, and basic observability.

## 🚀 Features
- FastAPI scoring API (`/score`) with Pydantic validation
- Simple feature engineering and a lightweight logistic model (pre-trained artifact included)
- Prometheus metrics (`/metrics`) and health checks (`/health`)
- Dockerfile + docker-compose for local run
- Helm chart for Kubernetes/OpenShift deployments
- CI with GitHub Actions + example Jenkinsfile
- Pytest tests

## 🧭 Structure
```
capgemini-rt-ml-platform/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── model.py
│   ├── features.py
│   ├── schemas.py
│   ├── logger.py
│   └── __init__.py
├── models/
│   ├── artifacts/model.pkl
│   └── train_dummy_model.py
├── infra/
│   └── helm/
│       └── capgemini-rt-ml-platform/
│           ├── Chart.yaml
│           ├── values.yaml
│           └── templates/
│               ├── deployment.yaml
│               ├── service.yaml
│               └── hpa.yaml
├── .github/workflows/ci.yml
├── tests/test_api.py
├── scripts/load_sample_requests.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🧪 Quickstart

### 1) Python (local)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```
Then open: `http://localhost:8080/docs`

### 2) Docker
```bash
docker build -t capgemini-rt-ml-platform:latest .
docker run -p 8080:8080 capgemini-rt-ml-platform:latest
```

### 3) Kubernetes with Helm
```bash
helm upgrade --install rt-ml infra/helm/capgemini-rt-ml-platform -n default
```

## 🧩 Sample Request
```bash
curl -X POST http://localhost:8080/score -H "Content-Type: application/json" -d '{
  "features": [0.3, -1.2, 0.5, 1.1, 0.0, -0.4]
}'
```

## 📊 Observability
- **/metrics**: Prometheus metrics (request count, latency histogram)
- **/health**: liveness check

## 🧪 Tests
```bash
pytest -q
```

## 📄 Notes
- The included model is a lightweight logistic function with random weights (AUC placeholder ~0.85) to keep the repo self-contained.
- To integrate a real MLflow model, replace `models/train_dummy_model.py` and `app/model.py` with MLflow loading logic.
