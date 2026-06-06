from fastapi import FastAPI, HTTPException, Form, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from duckduckgo_search import DDGS
import os

api_key_header = APIKeyHeader(name="ESCRUTA_INTERNAL_API_KEY", auto_error=False)


def verify_token(x_token: str = Security(api_key_header)):
    api_key = os.getenv("ESCRUTA_INTERNAL_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Server Configuration Error")

    if not x_token or x_token != api_key:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
    return x_token


app = FastAPI(dependencies=[Depends(verify_token)])


@app.post("/search")
async def search(query: str = Form(...), max_results: int = Form(10)):
    if not query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    if max_results < 1 or max_results > 50:
        raise HTTPException(status_code=400, detail="max_results must be between 1 and 50")

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Search provider error: {e}")

    return {
        "results": [
            {"title": r.get("title"), "link": r.get("href"), "snippet": r.get("body")}
            for r in results
        ]
    }
