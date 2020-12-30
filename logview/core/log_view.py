import sys

from core.syslog import LogStr, Syslog


def get_logs():
    """
    Returns logs on linux syslog file.
    TODO: 
        - Handle exception encoding error)
    """
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

# def format_logs(fn):
#     """
#     A decorator function that handle output style.
#     """
#     def wrapped():
#         output_log = fn()
#         syslog = Syslog(output_log)
#         return syslog.print_data()
#     return wrapped    

# @format_logs
def filter_log(**kwargs):
    """
    Filter syslog output by pid.
    """
    syslog = Syslog(get_logs())
    syslog.filter_log(**kwargs)
    print(syslog.log_print)

# @format_logs
def print_all():
    """
    Print all logs.
    """
    syslog = Syslog(get_logs())
    print(syslog.log_print)
