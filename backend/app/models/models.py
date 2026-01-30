from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Noticias(Base):
    __tablename__ = "noticias"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    titulo = Column(String(255), nullable=False)
    resumen = Column(Text, nullable=True)
    url = Column(Text, nullable=False, unique=True)
    fecha_publicacion = Column(DateTime, nullable=False)
    categoria = Column(String(50), nullable=True)
    fuente = Column(String(100), nullable=True)
    imagen = Column(Text, nullable=True)
