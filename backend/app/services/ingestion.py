from time import mktime
from feedparser import parse
from datetime import datetime, time

url = "https://www.libertaddigital.com/espana/rss.xml"


def ingesta(url):
    feed = parse(url)
    noticias = feed['entries']
    if not noticias:
        return noticias

    resultados = []

    for noticia in noticias:
        titulo = noticia.get('title')
        link = noticia.get('link')
        fecha = noticia.get('published')
        descripcion = noticia.get('description')

        if not titulo or not link:
            continue
        fecha_dt = datetime.strptime(fecha, "%a, %d %b %Y %H:%M:%S %z")
        fecha_normalizada = fecha_dt.strftime("%d/%m/%Y")

        resultados.append({
            "titulo": titulo,
            "link": link,
            "fecha": fecha_normalizada
        })
    return resultados


for notica in ingesta(url):
    print(notica)
