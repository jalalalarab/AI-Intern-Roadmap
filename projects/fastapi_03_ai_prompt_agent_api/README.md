\# AI Prompt/Tools API



Satisfies roadmap requirement: API + database + LLM/agent-style logging.



\## Stack

FastAPI, SQLModel, SQLite



\## How to run

uvicorn app:app --reload --port 8002

Visit http://127.0.0.1:8002/docs



\## Endpoints

\- POST /chat — rule-based response (placeholder for a real LLM), logs prompt+response

\- GET /chat-history — lists all chat logs

\- POST /tools/calculate — evaluates a simple math expression, logs the call

\- POST /tools/summarize — basic rule-based text summary, logs the call

\- GET /tools/history — lists all tool calls



\## What I learned

\- Separating conversation logs from tool-call logs into different tables

\- The "swap the logic, keep the architecture" pattern for going from rule-based to real LLM

\- Basic input sanitization when using eval() (whitelisting allowed characters)



\## Limitations

\- /chat is not connected to a real LLM yet — rule-based fallback only

\- eval() in /tools/calculate is restricted to a character whitelist but is not production-safe

