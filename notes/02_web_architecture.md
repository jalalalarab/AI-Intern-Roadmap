\# Web Architecture



\## API (Application Programming Interface)

\*\*Definition:\*\* A defined way for two programs to talk to each other — a set of rules for what requests you can send and what responses you'll get back.

\*\*Where used:\*\* Almost every modern app — mobile apps talking to servers, websites fetching data, services talking to other services.

\*\*Example:\*\* Our Task Tracker API — the client (Swagger UI / a frontend) sends requests, our FastAPI server responds with task data.

\*\*Key terms:\*\* endpoint, request, response, client, server.

\*\*Connection to internship:\*\* Built two working REST APIs (Projects 1 \& 2) with full CRUD and ML inference.



\## Endpoint

\*\*Definition:\*\* A specific URL + HTTP method combination that triggers one function on the server.

\*\*Example:\*\* `POST /tasks` (create) vs `GET /tasks` (list) — same URL text, different method, different behavior.



\## Request / Response

\*\*Definition:\*\* A request is what the client sends (method, URL, headers, optional body). A response is what the server sends back (status code, headers, body).

\*\*Example:\*\* `POST /predict` with 4 measurements in the body → response with predicted species + confidence.



\## HTTP Methods

\- \*\*GET\*\* — retrieve data, don't change anything (e.g. `GET /tasks`)

\- \*\*POST\*\* — create something new (e.g. `POST /tasks`)

\- \*\*PUT\*\* — update/replace an existing resource (e.g. `PUT /tasks/{id}`)

\- \*\*DELETE\*\* — remove a resource (e.g. `DELETE /tasks/{id}`)



\## Status Codes

\- \*\*200\*\* — success

\- \*\*404\*\* — Not Found: request was valid, but the thing requested doesn't exist (e.g. `GET /tasks/999`)

\- \*\*422\*\* — Unprocessable Entity: request body failed validation (e.g. wrong data type) — happens automatically via Pydantic before our code even runs



\## JSON

\*\*Definition:\*\* A lightweight text format for structuring data as key-value pairs — the standard format APIs use to send/receive data.

\*\*Example:\*\* `{"title": "Finish project", "status": "pending"}`



\## REST

\*\*Definition:\*\* A convention for designing APIs around resources (nouns, like "tasks") and standard HTTP methods (verbs) acting on them, rather than custom one-off endpoints for every action.

\*\*Example:\*\* Our Task API follows REST — `/tasks` is the resource, GET/POST/PUT/DELETE are the actions.



\## CRUD

\*\*Definition:\*\* Create, Read, Update, Delete — the four basic operations almost every data-backed app needs.

\*\*Connection to internship:\*\* This is exactly what Project 1 implements.



\## Long Polling vs WebSockets

\*\*Long polling:\*\* Client repeatedly sends requests asking "anything new?" — server holds the request open until there's new data (or a timeout), then responds; client immediately asks again. Simple, but inefficient for very frequent updates (constant request/response overhead).

\*\*WebSockets:\*\* A single persistent, two-way connection between client and server. Either side can send data anytime without re-establishing a connection each time. More efficient for real-time use cases (chat apps, live dashboards, live notifications).

\*\*Where used:\*\* Long polling — simpler real-time-ish needs, legacy systems. WebSockets — chat apps, live trading data, multiplayer games, collaborative editing.

\*\*Connection to internship:\*\* Neither was required as a build, but understanding the tradeoff (simplicity vs efficiency for real-time data) is a common interview topic when discussing API design.

