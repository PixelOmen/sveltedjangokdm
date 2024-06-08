import os
from uuid import uuid4
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass

from dotenv import load_dotenv
load_dotenv()

HTML_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
HUMAN_DATE_FORMAT = "%m/%d/%Y %H:%M"
CLI_BIN = os.getenv("KDM_CLI_BIN")

@dataclass
class KDMSession:
    jobid: str
    submitted: str
    cert: str
    dkdm: str
    html_start: str
    html_end: str
    timezone: str
    outputDir: str
    status: str = 'ok'
    error: str = ''
    human_start: str = ''
    human_end: str = ''
    kdm_name: str = ''
    kdm_path: str = ''

    def __post_init__(self):
        if self.html_start:
            self.human_start = self._html_to_human_date(self.html_start)
        if self.html_end:
            self.human_end = self._html_to_human_date(self.html_end)

    def as_dict(self) -> dict:
        session_dict = {k:v for k,v in self.__dict__.items() if k != "config"}
        if self.cert:
            session_dict["cert"] = Path(self.cert).name
        return session_dict

    def validate(self) -> None:
        if self.status != "ok":
            return
        if not self._validate_sources():
            return
        if not self._validate_dates():
            return
        if not self._validate_output_dir():
            return
        
    def set_error(self, msg: str) -> None:
        self.status = "error"
        self.error = msg        

    def cli_cmd(self) -> str:
        # r' -C "CERT.pem" -K "outputname" -o "OUTPUTDIR" -f "2024-03-21T17:41:00-07:00" -t "2024-03-21T19:41:00-07:00" "DKDM.xml"'
        clibin = f'"{CLI_BIN}"'
        start, end = self._cli_dates()
        cert = f'"{self.cert}"'
        dkdm = f'"{self.dkdm}"'
        outputdir = f'"{self.outputDir}"'
        self.kdm_name = self.gen_kdm_name()
        self.kdm_path = self.gen_kdm_path()
        return f"{clibin} -C {cert} -K {self.kdm_name} -o {outputdir} -f {start} -t {end} {dkdm}"
    
    def gen_kdm_name(self) -> str:
        self.kdm_name = f"KDM_{Path(self.dkdm).stem[:20]}-{Path(self.cert).stem[:20]}"
        return self.kdm_name
    
    def gen_kdm_path(self) -> str:
        stem = self.gen_kdm_name()[:100]
        self.kdm_path = str(Path(self.outputDir) / f"{stem}_{str(uuid4())[:6]}.xml")
        return self.kdm_path

    def _cli_dates(self) -> tuple[str, str]:
        tz_prefix = self.timezone[0]
        tz_padding = f"{int(self.timezone[1:]):02}:00"
        tz = tz_prefix + tz_padding
        start = f'"{self.html_start}:00{tz}"'
        end = f'"{self.html_end}:00{tz}"'
        return start, end
    
    def _html_to_human_date(self, datestr: str) -> str:
        dateobj = datetime.strptime(datestr, HTML_DATE_FORMAT)
        return dateobj.strftime(HUMAN_DATE_FORMAT)
    
    def _validate_sources(self) -> bool:
        if self.cert:
            if not Path(self.cert).is_file():
                self.set_error(f"Invalid Cert path: {self.cert}")
                return False
        if self.dkdm:
            if not Path(self.dkdm).is_file():
                self.set_error(f"Invalid DKDM path: {self.dkdm}")
                return False
        return True
    
    def _validate_output_dir(self) -> bool:
        Path(self.outputDir).mkdir(parents=True, exist_ok=True)
        if not Path(self.outputDir).is_dir():
            self.set_error(f"Not a valid directory: {self.outputDir}")
            return False
        return True

    def _validate_dates(self) -> bool:
        start = datetime.strptime(self.human_start, HUMAN_DATE_FORMAT)
        end = datetime.strptime(self.human_end, HUMAN_DATE_FORMAT)
        if end <= start:
            self.set_error("End time is less than or equal to Start time")
            return False
        return True