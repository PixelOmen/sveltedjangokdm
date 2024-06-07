import os
import subprocess as sub
from typing import Any
from datetime import datetime

from .kdmsession import KDMSession, HUMAN_DATE_FORMAT

# --- fronend payload
# {
#     "cert": '/mnt/my/cert.pem',
#     "dkdm": "/mnt/my/dkdm.xml",
#     "startDate": "2025-01-01T01:00",
#     "endDate": "2025-01-01T01:00",
#     "timezone": "-11",
#     "outputDir": "mnt/my/output/dir",
# }


def process_request(userdata: Any, jobid: str) -> KDMSession:
    if not isinstance(userdata, dict):
        return _bad_request(jobid)
    session = _create_sessions(userdata, jobid)
    session.validate()
    if session.status == "ok":
        _start_subprocess(session)
    return session

def _start_subprocess(kdmsession: KDMSession) -> None:
    cmd = kdmsession.cli_cmd()
    process = sub.Popen(cmd, stdout=sub.PIPE, stderr=sub.PIPE)
    _, stderr = process.communicate()
    if stderr:
        stderr_str = stderr.decode()
        if stderr_str:
            try:
                error = stderr_str.split(f"{str(os.getenv('clibin'))[1:-1]}: ")[1]
            except IndexError:
                error = stderr_str
            kdmsession.set_error(f"DCP-o-matic error:\n {error}")


def _now_str() -> str:
    return datetime.now().strftime(HUMAN_DATE_FORMAT)

def _bad_request(jobid: str, errmsg: str='') -> KDMSession:
    if not errmsg:
        errmsg = "Malformed JSON from frontend"
    return KDMSession(
        jobid=jobid,
        submitted=_now_str(),
        cert='',
        dkdm='',
        html_start='',
        html_end='',
        timezone='',
        outputDir='',
        status='error',
        error=errmsg
    )  
    
def _create_sessions(userdata: dict, jobid: str) -> KDMSession:
    try:
        start_str = userdata['startDate']
        end_str = userdata['endDate']
        cert_path = userdata['cert']
        dkdm_path = userdata['dkdm']
        timezone = userdata['timezone']
        outputDir = userdata['outputDir']
    except KeyError:
        return _bad_request(jobid)

    return KDMSession(
        jobid=jobid,
        submitted=_now_str(),
        cert=cert_path,
        dkdm=dkdm_path,
        html_start=start_str,
        html_end=end_str,
        timezone=timezone,
        outputDir=outputDir
    )