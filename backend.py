import os

import openai
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

load_dotenv(".env")

app = FastAPI()

templates = Jinja2Templates(directory="templates")

llm_client = openai.OpenAI(
    base_url=os.environ["OPENAI_API_BASE_URL"],
    api_key=os.environ["OPENAI_API_KEY"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    messages: list[Message]
    max_tokens: int
    logprobs: bool = True
    top_logprobs: int
    model_name: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat/completions")
async def chat_completion(request: ChatCompletionRequest):
    try:
        response = llm_client.chat.completions.create(
            model=request.model_name,
            messages=[message.dict() for message in request.messages],
            max_tokens=request.max_tokens,
            logprobs=request.logprobs,
            top_logprobs=request.top_logprobs,
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
