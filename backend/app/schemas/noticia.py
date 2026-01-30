from pydantic import BaseModel, ConfigDict
import datetime
import typing


class BaseNoticia(BaseModel):
    titulo: str
    resumen: str
    url: str


class CreateNoticia(BaseNoticia):
    clave_foranea: int


class ResponseNoticia(BaseNoticia):
    id: int
    fecha_publicacion: datetime.datetime
    categoria: str
    imagen: str
    fuente: str

    model_config = ConfigDict(from_attributes=True)
