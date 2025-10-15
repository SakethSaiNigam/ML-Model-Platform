import pickle, numpy as np
from .config import settings

def _sigmoid(z: float) -> float:
    return 1.0 / (1.0 + np.exp(-z))

class ModelService:
    def __init__(self, model_path: str = None):
        self.model_path = model_path or settings.MODEL_PATH
        self._meta = {}
        self._weights = None
        self._bias = 0.0
        self.load()

    def load(self):
        with open(self.model_path, "rb") as f:
            payload = pickle.load(f)
        self._weights = np.array(payload["weights"], dtype=float)
        self._bias = float(payload["bias"])
        self._meta = {k:v for k,v in payload.items() if k not in ("weights","bias")}

    def predict_proba(self, x: np.ndarray) -> float:
        z = float(np.dot(self._weights, x) + self._bias)
        return float(_sigmoid(z))

    @property
    def meta(self):
        return self._meta

model_service = ModelService()
