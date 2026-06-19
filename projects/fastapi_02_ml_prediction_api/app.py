from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select
from datetime import datetime
from typing import Optional
import joblib
import numpy as np

# ---- Database setup ----
DATABASE_URL = "sqlite:///./predictions.db"
engine = create_engine(DATABASE_URL, echo=False)

# ---- Load the trained model once, at startup ----
model = joblib.load("iris_model.joblib")
IRIS_SPECIES = ["setosa", "versicolor", "virginica"]

# ---- Data model for logging predictions ----
class PredictionLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    predicted_class: str
    confidence: float
    created_at: datetime = Field(default_factory=datetime.utcnow)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
def root():
    return {"message": "ML Prediction API running"}

@app.post("/predict")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    confidence = float(max(probabilities))
    predicted_species = IRIS_SPECIES[prediction]

    log_entry = PredictionLog(
        sepal_length=sepal_length,
        sepal_width=sepal_width,
        petal_length=petal_length,
        petal_width=petal_width,
        predicted_class=predicted_species,
        confidence=confidence,
    )
    with Session(engine) as session:
        session.add(log_entry)
        session.commit()
        session.refresh(log_entry)

    return {
        "predicted_species": predicted_species,
        "confidence": round(confidence, 3),
        "log_id": log_entry.id,
    }

@app.get("/predictions", response_model=list[PredictionLog])
def list_predictions():
    with Session(engine) as session:
        return session.exec(select(PredictionLog)).all()

@app.get("/model-info")
def model_info():
    return {
        "model_type": "LogisticRegression",
        "classes": IRIS_SPECIES,
        "features_required": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
    }