import httpx
from typing import Annotated
from fastapi import FastAPI, Request
from pydantic import BaseModel
from models import endpoints

class CompletionRequest(BaseModel):
    model: str
    messages: list

class CompletionResponseTest(BaseModel):
    model: str
    messages: list

app = FastAPI()

"""
Defining a POST endpoint /completions

Header and body should be structured exactly as it would be passed to OpenAI, Mistral, or Anthropic
Header will be passed as given
Request authentication is done automatically by FastAPI
"""
@app.post("/completions/")
def completions(item: CompletionRequest, request: Request) -> CompletionResponseTest:
    model = item.model
    if model not in endpoints:
        return BaseException

    response = httpx.post(
        endpoints[model], 
        data={
            "model": item.model,
            "messages": item.messages,
        },
        headers=request.headers
    )

    return response

@app.post("/test/")
def test(item: CompletionRequest, request: Request) -> CompletionResponseTest:
    print(request.headers)
    return item

"""
OpenAI: Authorization: Bearer [token]
Mistral: Authorization: Bearer [token]
Claude: x-api-key: [token]
"""