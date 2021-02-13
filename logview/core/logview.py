import csv

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
    with open("/var/log/syslog", "r") as data:
        current = data.readline()
        while current:
            try:
                logs.append(current)
                current = data.readline()
            except UnicodeDecodeError:
                continue
    return logs


SYSLOG = Syslog(get_logs())


@option_description("filter", "-f", "Filter syslog output")
def filter_logs(syslog=SYSLOG, **kwargs) -> None:
    """
    Filter syslog output.
    """
    logs = syslog.logs_list
    for key, value in kwargs.items():
        if key == "pid":
            logs = [log for log in logs if value in log["source"]]
        else:
            logs = [log for log in logs if value in log[key]]
    if logs:
        print(syslog.print_logs(logs))
    else:
        print("There is no search results.")


def print_all(syslog=SYSLOG) -> None:
    """
    Print all logs.
    """
    print(syslog)


def sorting(syslog=SYSLOG, *args) -> None:
    """
    Sort logs by args (date, source, event, user).
    """
    logs = sorted(syslog.logs_list, key=lambda x: x[args[0]])
    print(syslog.print_logs(logs))


def to_csv(syslog=SYSLOG):
    logs = syslog.log_list
    with open("syslog.csv", "w", newline=" ") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for log in logs:
            writer.writerow([log.date, log.user, log.source, log.event])
    print("Completed!")


def to_excel(syslog=SYSLOG):
    pass


def to_json(syslog=SYSLOG):
    pass


def to_pdf():
    pass
