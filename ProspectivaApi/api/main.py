from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from service import generate_response
from typing import Dict

app = FastAPI()
@app.post("/prospectiva")
async def root(data: Dict) -> PlainTextResponse:
    
    return generate_response(data)