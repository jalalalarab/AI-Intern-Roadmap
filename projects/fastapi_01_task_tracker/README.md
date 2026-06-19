\# Task Tracker API



Satisfies roadmap requirement: APIs — FastAPI + database project (CRUD).



\## Stack

FastAPI, SQLModel, SQLite



\## How to run

cd projects/fastapi\_01\_task\_tracker

uvicorn app:app --reload

Visit http://127.0.0.1:8000/docs



\## Endpoints

\- POST /tasks — create a task

\- GET /tasks — list all tasks

\- GET /tasks/{id} — get one task (404 if missing)

\- PUT /tasks/{id} — update a task

\- DELETE /tasks/{id} — delete a task



\## What I learned

\- How FastAPI routes requests by method + path

\- Pydantic/SQLModel automatic request validation (422 on bad input)

\- SQLModel session pattern: add → commit → refresh

\- Manual 404 handling with HTTPException

