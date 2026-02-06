from time import mktime
from feedparser import parse
from datetime import datetime, time
import html


def ingesta(url):
    feed = parse(url)
    canal = feed.get('channel', {}).get('title', 'Fuente desconocida')
    noticias = feed['entries']
    if not noticias:
        return noticias

    resultados = []

    for noticia in noticias:
        titulo = html.unescape(noticia.get('title', ""))
        url = noticia.get('link')
        fecha = noticia.get('published')
        descripcion = html.unescape(noticia.get('description', ""))
        categoria = noticia.get("category") or "General"
        media = noticia.get("media_content")
        imagen = None

        if not titulo or not url:
            continue

        # Procesar fecha con manejo de errores
        fecha_dt = None
        if fecha:
            try:
                # Reemplazar GMT con +0000 para compatibilidad con %z
                fecha_limpia = fecha.replace("GMT", "+0000")
                fecha_dt = datetime.strptime(
                    fecha_limpia, "%a, %d %b %Y %H:%M:%S %z")
            except (ValueError, AttributeError):
                fecha_dt = datetime.now()
        else:
            fecha_dt = datetime.now()

        if media and len(media) > 0:
            imagen = media[0].get('url')

        # Convertir categoría a string si es un objeto
        if categoria and hasattr(categoria, 'term'):
            categoria = categoria.get('term', None)
        elif isinstance(categoria, dict):
            categoria = categoria.get('term', None)

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
