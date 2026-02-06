from pydantic import BaseModel, ConfigDict
import datetime
from typing import Optional


class BaseNoticia(BaseModel):
    titulo: str
    resumen: str
    url: str


class CreateNoticia(BaseNoticia):
    clave_foranea: int


class ResponseNoticia(BaseNoticia):
    id: int
    fecha_publicacion: datetime.datetime
    categoria: Optional[str] = "General"
    imagen: str | None = None
    fuente: str

    model_config = ConfigDict(from_attributes=True)
