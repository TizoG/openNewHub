from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from ..models.models import Noticias


def borrar_noticias_antiguas(db: Session, dias: int = 5):
    """
    Elimina las noticias que sean más antiguas que el numero especificado.
    """
    fecha_limite = datetime.now()-timedelta(days=dias)

    print(
        f"Iniciando limpieza: Borrando noticias anteriores a {fecha_limite}...")

    cantidad_borrada = db.query(Noticias).filter(
        Noticias.fecha_publicacion < fecha_limite).delete()

    db.commit()

    print(
        f"Limpieza completada. Se han eliminado {cantidad_borrada} noticias.")
