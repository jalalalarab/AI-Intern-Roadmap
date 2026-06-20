from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from datetime import datetime
from typing import Optional

# ---- Database setup ----
DATABASE_URL = "sqlite:///./agent_api.db"
engine = create_engine(DATABASE_URL, echo=False)

# ---- Data models ----
class PromptLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    prompt: str
    response: str
    model_name: str = "rule-based-fallback"
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ToolCall(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tool_name: str
    input: str
    output: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
def root():
    return {"message": "AI Prompt/Tools API running"}

# ---- Chat endpoint (rule-based fallback, logged like a real LLM call) ----
@app.post("/chat")
def chat(prompt: str):
    # Rule-based fallback response (no live LLM connected).
    # The point being proven here is the logging pattern, not a smart model.
    response_text = f"[Rule-based response] You said: '{prompt}'. " \
                     f"This would normally be sent to an LLM (e.g. OpenAI, Claude) for a real reply."

    log_entry = PromptLog(prompt=prompt, response=response_text)
    with Session(engine) as session:
        session.add(log_entry)
        session.commit()
        session.refresh(log_entry)

    return {"prompt": prompt, "response": response_text, "log_id": log_entry.id}

@app.get("/chat-history", response_model=list[PromptLog])
def chat_history():
    with Session(engine) as session:
        return session.exec(select(PromptLog)).all()

# ---- Tool 1: calculator ----
@app.post("/tools/calculate")
def calculate(expression: str):
    try:
        # NOTE: eval() is used here only for a controlled internal demo on
        # simple arithmetic strings. Never use eval() on untrusted input
        # in a real production system - this is a known security risk.
        allowed_chars = set("0123456789+-*/(). ")
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Invalid characters in expression")
        result = eval(expression)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not evaluate expression: {e}")

    log_entry = ToolCall(tool_name="calculate", input=expression, output=str(result))
    with Session(engine) as session:
        session.add(log_entry)
        session.commit()
        session.refresh(log_entry)

    return {"expression": expression, "result": result, "log_id": log_entry.id}

# ---- Tool 2: keyword summarizer (simple, rule-based) ----
@app.post("/tools/summarize")
def summarize(text: str):
    words = text.split()
    word_count = len(words)
    # Very simple "summary": first sentence + word count.
    first_sentence = text.split(".")[0].strip() + "." if "." in text else text
    summary = f"{first_sentence} (Full text: {word_count} words)"

    log_entry = ToolCall(tool_name="summarize", input=text, output=summary)
    with Session(engine) as session:
        session.add(log_entry)
        session.commit()
        session.refresh(log_entry)

    return {"original_word_count": word_count, "summary": summary, "log_id": log_entry.id}

@app.get("/tools/history", response_model=list[ToolCall])
def tools_history():
    with Session(engine) as session:
        return session.exec(select(ToolCall)).all()