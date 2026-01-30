from apscheduler.schedulers.background import BackgroundScheduler


from ..db.connection import sesion
from ..services.noticie_service import servicio_noticias


def tarea_programada():
    session_manual = sesion()
    servicio_noticias(session_manual)
    session_manual.close()


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tarea_programada, 'interval', hours=12)
    scheduler.start()
