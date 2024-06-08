import time
from pathlib import Path
from threading import Thread
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models import KDM


# This module should be replaced with Celery tasks in a production environment

def _work_thread(kdm: "KDM", delay: int):
    time.sleep(delay)
    kdm.file.delete(False)

def delete_after_delay(kdm: "KDM", delay: int = 30) -> None:
    Thread(target=_work_thread, args=(kdm, delay)).start()

