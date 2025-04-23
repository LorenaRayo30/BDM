from fastapi import APIRouter
from app.models.Request import RequestData

router = APIRouter()

@router.get("/")
def Consult_Agent():
    return [{"id": 1, "name": "Juan"}, {"id": 2, "name": "María"}]

@router.post("/")
def Consult_Database(user: RequestData):
    return {"mensaje": f"Usuario {user.name} creado con éxito"}
