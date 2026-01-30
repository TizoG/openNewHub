from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .services.noticie_service import servicio_noticias
from .db.connection import sesion

from .api.noticias import router
from .db.connection import engine
from .models.models import Base,  Noticias

from .services.scheduler import start_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- TODO LO QUE VA AQUÍ SE EJECUTA AL ARRANCAR ---
    print("🚀 Arrancando la aplicación...")

    # 1. Iniciamos el reloj de las 12 horas
    start_scheduler()

    # 2. Ejecutamos la primera ingesta manual para no esperar 12 horas
    db = sesion()
    try:
        print("📥 Ejecutando ingesta inicial de noticias...")
        servicio_noticias(db)
    finally:
        db.close()

    yield  # Aquí es donde la App se queda "viva" y esperando peticiones

    # --- TODO LO QUE VA AQUÍ SE EJECUTA AL APAGAR ---
    print("🛑 Apagando la aplicación...")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router, prefix="/noticias")

Base.metadata.create_all(bind=engine)
