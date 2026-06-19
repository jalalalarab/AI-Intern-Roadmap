\# ML Prediction API



Satisfies roadmap requirement: APIs + database + ML deployment.



\## Stack

FastAPI, scikit-learn, joblib, SQLModel, SQLite



\## How to run

1\. Train the model (one-time): python train\_model.py

2\. Start the API: uvicorn app:app --reload --port 8001

3\. Visit http://127.0.0.1:8001/docs



\## Model

Logistic Regression trained on the Iris dataset (150 samples, 3 species).

Test accuracy: 1.00 (expected — Iris is a small, easily separable dataset)



\## Endpoints

\- POST /predict — takes 4 flower measurements, returns predicted species + confidence, logs to DB

\- GET /predictions — lists all logged predictions

\- GET /model-info — returns model type and required features



\## What I learned

\- Train/test split prevents evaluating a model on data it already memorized

\- predict() vs predict\_proba() — final answer vs per-class confidence

\- Loading a serialized model once at startup instead of per-request

\- Logging ML predictions to a database for traceability



\## Limitations

\- No input validation on measurement ranges (could accept nonsensical values)

\- Single fixed model — no retraining/versioning endpoint

