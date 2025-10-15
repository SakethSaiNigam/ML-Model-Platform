from pydantic import BaseModel, Field, conlist

class ScoreRequest(BaseModel):
    features: conlist(float, min_length=6, max_length=6) = Field(..., description="Six numeric features")

class ScoreResponse(BaseModel):
    score: float
    model_auc: float
    model_trained_at: str
