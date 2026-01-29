from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.noticias import router
from .db.connection import engine
from .models.models import Base, Fuentes, Noticias


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router, prefix="/noticias")
