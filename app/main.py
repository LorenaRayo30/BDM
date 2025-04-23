from fastapi import FastAPI
from app.routes import Upload, Manipulation, Consult

app = FastAPI(
    title="XM ApiRestful",
    description="Api Restful para el consumo y manipulación de datos en Local para la empresa XM.",
    redoc_url="/documentacion",
    docs_url=None,
    Version="1.0.0"
    )

# Registrar rutas
app.include_router(Upload.router, prefix="/Upload", tags=["Cargar datos"])

app.include_router(Manipulation.router, prefix="/Manipulation", tags=["Manipulación de los datos"])

app.include_router(Consult.router, prefix="/Consults", tags=["Manipulación de los datos"])