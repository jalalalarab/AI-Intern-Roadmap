# AI Engineering Study Log

My personal study log for the AI-engineering roadmap I was given as an
AI Engineering Intern at **EDM (Engineering Design & Manufacturing)**,
Beirut, in June 2026. The roadmap was designed and assigned by my
instructor **Omar Baayoun**; this repository is my execution of it —
the notebooks I ran and the projects I built.

Published with permission.

---

## Context

The roadmap runs as a short, high-intensity sprint covering the
foundations an AI engineer is expected to be fluent in — programming
and data, machine learning, generative AI and LLMs, and productionising
models behind an API. Rather than reading passively, the plan is
organised around **four required builds**, plus explaining each topic
back in the candidate's own words.

This repository is what I actually produced going through it.

---

## The four required builds (all in `projects/`)

| # | Project | Stack | What it demonstrates |
|---|---|---|---|
| 1 | **Task Tracker API** | FastAPI, SQLModel, SQLite | Full CRUD with route-by-method design, automatic Pydantic validation, and manual 404 handling |
| 2 | **ML Prediction API** | FastAPI, scikit-learn, joblib, SQLModel, SQLite | Train a logistic-regression classifier on Iris, serialise it, load once at startup, serve predictions with confidence, and log every call to a database for traceability |
| 3 | **AI Prompt / Tools API** | FastAPI, SQLModel, SQLite | Separate conversation and tool-call logs into distinct tables; two simple tools (`calculate`, `summarize`); the "swap the logic, keep the architecture" pattern that lets a rule-based endpoint become a real-LLM endpoint without moving the plumbing |
| 4 | **Computer Vision App** | OpenCV, DeepFace, TensorFlow (Google Colab) | Haar Cascade face detection with OpenCV, then DeepFace analysis for age / gender / emotion. Local install stalled — pivoted to Colab as the plan's backup strategy explicitly allows |

Each project folder has its own README with the stack, the endpoints,
what I learned, and — importantly — the limitations I'd fix before
calling it production. Screenshots of the working responses live in
`screenshots/`.

Two extras beyond the required four:

- **`react_agent_from_scratch/`** — a ReAct-style agent built from
  scratch in two notebooks: a single-turn version, then a looped
  version that keeps reasoning + acting until it reaches an answer.
- **`llm_tools_demos/`** — HuggingFace pipeline demos (sentiment
  classification and text generation) showing tool usage against
  hosted models.

## Notebooks (`notebooks/`)

- `ml_overview.ipynb` — the machine-learning overview: EDA on a sample
  dataset (age distribution), K-means clustering with cluster profiles,
  and a supervised-learning model comparison. Output plots are in
  `screenshots/` (`ml_eda_age_distribution.png`,
  `ml_kmeans_cluster_profiles.png`, `ml_model_comparison_scores.png`).

## Screenshots (`screenshots/`)

Proof-of-working screenshots for every project — the FastAPI Swagger
routes, correct 200/404 responses, ML prediction outputs, CV face
detection and DeepFace analysis, HuggingFace demo output, and the
ML notebook plots. Referenced from the project READMEs.

---

## Tech stack across the repository

- **Language:** Python 3
- **APIs:** FastAPI, Uvicorn, SQLModel, Pydantic, SQLite
- **ML:** scikit-learn (logistic regression, K-means), joblib for
  model serialisation, pandas, matplotlib, seaborn
- **Computer vision:** OpenCV (Haar Cascades), DeepFace, TensorFlow
  (via Google Colab)
- **LLM demos:** HuggingFace transformers pipelines
- **Notebooks:** Jupyter

See `requirements.txt` for the exact pinned set.

## Run any project locally

Each project folder is self-contained. From the repo root:

```bash
python -m venv .venv
source .venv/bin/activate           # macOS/Linux
# .\.venv\Scripts\Activate.ps1      # Windows PowerShell
pip install -r requirements.txt

# then, for example:
cd projects/fastapi_01_task_tracker
uvicorn app:app --reload
# open http://127.0.0.1:8000/docs
```

The three FastAPI projects deliberately run on different ports (8000,
8001, 8002) so all three can run at the same time. The CV project runs
in Google Colab — open `projects/cv_deepface_app/cv_deepface_app.ipynb`.

## What this repo is — and isn't

**Is:** an honest record of a short, focused sprint through the
foundations of AI engineering, executed on a schedule, with every
project shipped to a working endpoint or notebook. The point was
breadth with a few areas of real depth, and being able to explain
every piece rather than only reproduce it.

**Isn't:** a production system. Several of the READMEs call out real
limitations — the AI Prompt/Tools API's `/chat` endpoint is a
placeholder for a real LLM, the ML API has no measurement-range
validation, the CV app was Colab-only. Those are acknowledged, not
hidden.

---

## Attribution

The roadmap and its four required builds were designed by my
instructor **Omar Baayoun** at EDM, Beirut. The work in this
repository is my own execution of that plan; published with his
permission.
