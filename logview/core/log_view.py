import sys

from core.syslog import Syslog


with open('/var/log/syslog', 'r') as data:
    SYSLOG = data.read()

def format_logs(fn):
    def wrapped():
        output_log = fn()
        syslog = Syslog(output_log)
        return syslog.print_data()
    return wrapped    

@format_logs
def filter_pid(filter_option: str):
    pass

@format_logs
def print_all():
    return SYSLOG
