import sys

from .syslog import Syslog


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
    Filter syslog output.
    """
    syslog = Syslog(get_logs())
    logs = syslog.logs_list
    for key, value in kwargs.items():
        if key == 'pid':
            logs = [log for log in logs if value in log['source']]
        else:
            logs = [log for log in logs if value in log[key]]
    if logs:
        print(syslog.print_logs(logs))
    else:
        print("There is no search results.")

def print_all() -> None:
    """
    Print all logs.
    """
    syslog = Syslog(get_logs())
    print(syslog)

def sorting(*args):
    syslog = Syslog(get_logs())
    logs = sorted(syslog.logs_list, key=lambda x: x[args[0]])
    print(syslog.print_logs(logs))

def merge_sort(logs: list, option):
    size_list = len(logs)

    if size_list < 2:
        return logs[0]
    
    list1, list2 = list(), list()

    for i in range(0,size_list//2):
        list1.append(logs.pop())

    while logs:
        list2.append(logs.pop())

    merge_sort(list1, option)
    merge_sort(list2, option)
    merge(logs, list1, list2, option)

def merge(logs, list1, list2, option):
    for i in range(len(list1)):
        if list1[i][option] > list2[i][option]:
            logs.append(list2.pop(i))
    while list1:
        logs.append(list1.pop())
    while list2:
        logs.append(list2.pop())


def to_csv():
    pass

def to_excel():
    pass

def to_json():
    pass

def to_pdf():
    pass