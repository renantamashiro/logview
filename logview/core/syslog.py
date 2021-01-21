from typing import Optional


class Syslog:
    def __init__(self, logs):
        self._logs = logs
        self._logs_list = self.build_logs_list()
        
    def __str__(self) -> str:
        return self.print_logs()
    
    @property
    def logs(self) -> list:
        """
        Getter method that returns syslog without format.
        """
        return self._logs
    
    @logs.setter
    def logs(self, logs: list) -> None:
        """
        Setter method that changes syslog data.
        """
        if isinstance(logs, list):
            self._logs = logs
        else:
            raise TypeError("`logs` must be a list instance")
    
    @property
    def logs_list(self) -> list:
        """
        Getter method that returns syslog list.
        """
        return self._logs_list

    @logs_list.setter
    def logs_list(self, logs_list: list) -> None:
        """
        Setter method that changes syslog list.
        """
        if isinstance(logs_list, list):
            self._logs_list = logs_list
        else:
            raise TypeError("`logs_list` must be a list instance")

    def build_logs_list(self) -> list:
        """
        Returns a list of dicts organized by date, user, source, and event.
        """
        log_list = list()
        for log in self.logs:
            try:
                date = log[:15]
                event_loc = log[16:].find(":") + 16
                user, source = log[16:event_loc].split(" ")
                event = log[event_loc+1:]
                log_list.append({
                    "date": date,
                    "user": user,
                    "source": source,
                    "event": event
                    })
            except ValueError:
                continue
        return log_list

    def print_logs(self, logs: Optional=None) -> str:
        """
        Print log data without format.
        """
        logs = logs if logs != None else self.logs_list
        logs_output = list()
        for log in logs:
            logs_output.append(f"{log['date'].center(16)}"
                               f"|{log['user'].center(12)}"
                               f"|{log['source'].center(20)}"
                               f"|{log['event']}")
        return '\n'.join(logs_output)   
