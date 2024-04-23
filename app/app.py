import httpx
from typing import Optional, Any
from fastapi import FastAPI, Request
from pydantic import BaseModel
from models import endpoints, authHeaders

class CompletionRequest(BaseModel):
    model: str
    messages: Optional[list] = None
    prompt: Optional[str] = None
    max_tokens_to_sample: Optional[int] = None

app = FastAPI()

"""
Defining a POST endpoint /completions

Header and body should be structured exactly as it would be passed to OpenAI, Mistral, or Anthropic
Header will be passed as given
Request authentication is done automatically by FastAPI
"""
@app.post("/completions/")
def completions(item: CompletionRequest, request: Request)-> Any:
    model = item.model
    json = {}
    if model not in endpoints:
        return BaseException
    elif model == 'claude-2.1':
        json={
            "model": item.model,
            "prompt": item.prompt,
            "max_tokens_to_sample": item.max_tokens_to_sample
        }
    else:
        json={
            "model": item.model,
            "messages": item.messages,
        }
    
    response = httpx.post(
        endpoints[model],
        json=json,
        headers={authHeaders[model]: request.headers[authHeaders[model]]},
    )

    return response.json()

"""
OpenAI: Authorization: Bearer [token]
Mistral: Authorization: Bearer [token]
Claude: x-api-key: [token]
"""