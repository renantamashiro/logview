import sys

from core.syslog import Syslog


def get_logs():
    with open('/var/log/syslog', 'r') as data:
        try:
            syslog_data = data.read()
        except UnicodeDecodeError:
            current = data.readline()
            syslog_data = list()
            while(current):
                syslog_data.append(current)
                try:
                    current = data.readline()
                except UnicodeDecodeError:
                    continue
            syslog_data = ''.join(syslog_data)
        finally:
            return syslog_data

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
    return get_logs()
