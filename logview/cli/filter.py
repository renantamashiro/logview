from logview.cli.logs import syslog
from logview.cli.models.usage import option_description


class Filter:
    @option_description("filter", "-f", "Filter syslog output")
    @syslog
    def filter_logs(syslog, *args, **kwargs) -> None:
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
