import time
from pathlib import Path
from threading import Thread

def _work_thread(userdir: Path, delay: int):
    time.sleep(delay)
    userdir.unlink(missing_ok=True)

def delete_after_delay(file_path: Path | str, delay: int = 30) -> None:
    file_path = Path(file_path)
    Thread(target=_work_thread, args=(file_path, delay)).start()

