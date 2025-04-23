from fastapi import APIRouter
from app.models.Request import RequestData
import httpx
from app.config.settings import OLLAMA_URL

router = APIRouter()

@router.post("/ask")
async def MakingQuery(data: RequestData):
    answer = await ConsultingLLM(data)
    return {"result":answer}

async def ConsultingLLM(data: RequestData):
    payload  = {
        "model": data.model,
        "prompt": data.body,
        "stream": data.stream
    }
    async with httpx.AsyncClient() as Client:
        response= await Client.post(OLLAMA_URL,json=payload)
    
    return response.json()