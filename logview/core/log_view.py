import sys

from core.syslog import Syslog


def config():
    """
    Config daemon thread to catch syslog data periodically
        attr: initial time, end time, period
    """
    pass

def daemon():
    """
    Set a deamon process to catch syslog data.
    """
    pass

def get_logs() -> list:
    """
    Returns logs on linux syslog file.
    TODO: 
        - Handle exception encoding error)
    """
    logs = list()
    with open('/var/log/syslog', 'r') as data:
        current = data.readline()
        while current:
            try:
                logs.append(current)
                current = data.readline()
            except UnicodeDecodeError as err:
                continue
    return logs

def filter_logs(**kwargs) -> None:
    """
    Filter syslog output by pid.
    """
    syslog = Syslog(get_logs())
    syslog.filter_logs(**kwargs)

def print_all() -> None:
    """
    Print all logs.
    """
    syslog = Syslog(get_logs())
    syslog.print_logs()

def sorting():
    pass

def to_csv():
    pass

def to_excel():
    pass

def to_json():
    pass

def to_pdf():
    pass