from time import mktime
from feedparser import parse
from datetime import datetime, time
import html


def ingesta(url):
    feed = parse(url)
    canal = feed['channel']['title']
    noticias = feed['entries']
    if not noticias:
        return noticias

    resultados = []

    for noticia in noticias:
        titulo = html.unescape(noticia.get('title', ""))
        url = noticia.get('link')
        fecha = noticia.get('published')
        descripcion = html.unescape(noticia.get('description', ""))
        categoria = noticia.get("category")
        media = noticia.get("media_content")
        imagen = None

        if not titulo or not url:
            continue
        fecha_dt = datetime.strptime(fecha, "%a, %d %b %Y %H:%M:%S %z")
        # fecha_normalizada = fecha_dt.strftime("%d/%m/%Y")
        if media and len(media) > 0:
            imagen = media[0].get('url')

        resultados.append({
            "titulo": titulo,
            "url": url,
            "fecha": fecha_dt,
            "resumen": descripcion,
            "categoria": categoria,
            "imagen": imagen,
            "fuente": canal
        })
    return resultados
