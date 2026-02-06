from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db.connection import db_get
from ..models.models import Noticias
from ..schemas.noticia import ResponseNoticia
from ..db.connection import sesion

router = APIRouter()


@router.get("/", response_model=List[ResponseNoticia])
def noticias(db: Session = Depends(db_get)):
    db_notias = db.query(Noticias).order_by(
        Noticias.fecha_publicacion.desc()).all()
    return db_notias


@router.get("/politica", response_model=List[ResponseNoticia])
def noticas_politica(db: Session = Depends(db_get)):
    db_notias = db.query(Noticias).filter(Noticias.categoria == "Política").order_by(
        Noticias.fecha_publicacion.desc()).all()
    return db_notias


@router.get("/internacional", response_model=List[ResponseNoticia])
def noticas_politica(db: Session = Depends(db_get)):
    db_notias = db.query(Noticias).filter(Noticias.categoria == "Internacional").order_by(
        Noticias.fecha_publicacion.desc()).all()
    return db_notias


@router.get("/tecnologia", response_model=List[ResponseNoticia])
def noticas_politica(db: Session = Depends(db_get)):
    db_notias = db.query(Noticias).filter(Noticias.categoria == "Tecnología").order_by(
        Noticias.fecha_publicacion.desc()).all()
    return db_notias


@router.get("/finanzas", response_model=List[ResponseNoticia])
def noticas_politica(db: Session = Depends(db_get)):
    db_notias = db.query(Noticias).filter(Noticias.categoria == "Finanzas").order_by(
        Noticias.fecha_publicacion.desc()).all()
    return db_notias


@router.get("/deportes", response_model=List[ResponseNoticia])
def noticas_politica(db: Session = Depends(db_get)):
    db_notias = db.query(Noticias).filter(Noticias.categoria == "Deportes").order_by(
        Noticias.fecha_publicacion.desc()).all()
    return db_notias


@router.get("/ciencia", response_model=List[ResponseNoticia])
def noticas_politica(db: Session = Depends(db_get)):
    db_notias = db.query(Noticias).filter(Noticias.categoria == "Ciencia").order_by(
        Noticias.fecha_publicacion.desc()).all()
    return db_notias


@router.get("/cultura", response_model=List[ResponseNoticia])
def noticas_politica(db: Session = Depends(db_get)):
    db_notias = db.query(Noticias).filter(Noticias.categoria == "Cultura").order_by(
        Noticias.fecha_publicacion.desc()).all()
    return db_notias
