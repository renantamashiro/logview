from logview.cli.models.syslog import Syslog


def get_logs(file_log: str) -> list:
    """
    Returns logs on linux syslog file.
    """

    logs = list()
    with open(f"/var/log/{file_log}", "r") as data:
        current = data.readline()
        while current:
            try:
                logs.append(current)
                current = data.readline()
            except UnicodeDecodeError:
                continue
    return logs


def syslog(function):
    def inner_function(*args, **kwargs):
        syslog = Syslog(get_logs("syslog"))
        function(syslog, *args, **kwargs)
    return inner_function
