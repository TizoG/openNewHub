from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Fuentes(Base):
    __tablename__="fuentes"
    id=Column(Integer,  autoincrement=True,index=True, primary_key=True)
    nombre_fuente=Column(String(150),nullable=True)
    url_fuente=Column(Text,unique=True, nullable=False)
    noticia=relationship("Noticias", back_populates="fuente")


class Noticias(Base):
    __tablename__="noticias"
    id=Column(Integer, primary_key=True, autoincrement=True,index=True)
    titulo=Column(String(255), nullable=False)
    resumen=Column(Text, nullable=True)
    url=Column(Text, nullable=False, unique=True)
    fecha_publicacion=Column(DateTime, nullable=False)
    clave_foranea=Column(Integer, ForeignKey("fuentes.id"), nullable=False)
    fuente=relationship("Fuentes",back_populates="noticia")
