# 📰 Open News Hub

Agregador de noticias open-source desarrollado con **Astro** y **FastAPI**, orientado a mostrar noticias actualizadas en español a partir de fuentes públicas (RSS y APIs de noticias).

El proyecto está diseñado como una base sólida y escalable para portales informativos modernos, priorizando buenas prácticas de arquitectura, legalidad del contenido y rendimiento.

---

## 🚀 Objetivo del proyecto

Construir un portal de noticias que:

- Agregue noticias de **actualidad general** y **tecnología / IA**
- Se actualice automáticamente varias veces al día
- Muestre solo contenido permitido (título, extracto y enlace)
- Respete los derechos de autor enlazando siempre a la fuente original
- Sirva como **proyecto profesional de portfolio open-source**

---

## 🧱 Stack tecnológico

### Frontend
- **Astro**
- **Tailwind CSS**
- Renderizado híbrido (SSR / SSG)
- Enfoque en rendimiento y SEO

### Backend
- **FastAPI**
- Python 3.11+
- APIs REST
- Tareas programadas (cron)

### Base de datos
- **PostgreSQL**
- SQLAlchemy ORM

---

## 📰 Fuentes de noticias

### Actualidad general
- RSS oficiales de medios en español (El País, RTVE, BBC Mundo, etc.)

### Tecnología e IA
- APIs públicas de noticias con soporte en español
- Filtros por categoría y palabras clave

> ⚠️ El proyecto **no almacena ni reproduce el contenido completo de las noticias**.  
> Solo se guardan metadatos y extractos cortos proporcionados por las fuentes.

---

## 📦 Funcionalidades (MVP)

- Importación automática de noticias desde:
  - Feeds RSS
  - APIs de noticias
- Normalización de datos entre múltiples fuentes
- Eliminación de noticias duplicadas
- Clasificación por categoría
- Portal web con:
  - Noticias del día
  - Secciones temáticas
  - Enlaces directos a la fuente original

---

## 🗂️ Modelo de datos

```text
News
├── id
├── title
├── excerpt
├── url
├── source
├── category
├── language
├── published_at
└── created_at
