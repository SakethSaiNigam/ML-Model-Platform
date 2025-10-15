import pickle, numpy as np
from datetime import datetime

def train(output_path: str = "models/artifacts/model.pkl", seed: int = 42):
    rng = np.random.default_rng(seed)
    weights = rng.normal(size=(6,)).astype(float)
    bias = float(rng.normal())
    payload = {"type":"dummy-logistic","weights":weights,"bias":bias,"trained_at":datetime.utcnow().isoformat(),"auc":0.85}
    with open(output_path, "wb") as f:
        pickle.dump(payload, f)
    print(f"Saved dummy model to {output_path}")

if __name__ == "__main__":
    train()
