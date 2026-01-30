
from ..db.connection import sesion
from ..services.ingestion import ingesta
from .urls_rss import URL_RSS_LIBERTAD
from ..models.models import Noticias


def servicio_noticias(sesion):
    noticias = ingesta(URL_RSS_LIBERTAD)
    nuevas_noticias = []
    for noticia in noticias:
        db_noticia = sesion.query(Noticias).filter(
            Noticias.url == noticia["url"]).first()
        if not db_noticia:
            nueva_noticia = Noticias(
                titulo=noticia["titulo"],
                resumen=noticia["resumen"],
                url=noticia["url"],
                fecha_publicacion=noticia["fecha"],
                categoria=noticia["categoria"],
                imagen=noticia["imagen"],
                fuente=noticia["fuente"]
            )
            nuevas_noticias.append(nueva_noticia)
    sesion.add_all(nuevas_noticias)
    sesion.commit()
