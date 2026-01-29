from typing import List
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from ..db.connection import db_get
from ..models.models import Noticias
from ..schemas.noticia import ResponseNoticia
from ..db.connection import sesion

router = APIRouter()

@router.get("/", response_model=List[ResponseNoticia])
def noticias(db:Session= Depends(db_get)):
    db_notias=db.query(Noticias).order_by(Noticias.fecha_publicacion.desc()).all()
    return db_notias

