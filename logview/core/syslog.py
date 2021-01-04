class Syslog:
    def __init__(self, logs):
        self._logs = logs
        self._logs_list_format = self.build_logs_list_format()
        
    def __str__(self) -> str:
        logs = list()
        for log in self.logs_list_format:
            logs.append(f"{log['date'].center(16)}"
                        f"|{log['user'].center(12)}"
                        f"|{log['source'].center(20)}"
                        f"|{log['event']}")
        return '\n'.join(logs)
    
    @property
    def logs(self) -> str:
        """
        Getter method that returns syslog without format.
        """
        return self._logs
    
    @logs.setter
    def logs(self, logs: str) -> None:
        """
        Setter method that changes syslog data.
        """
        self._logs = logs
    
    @property
    def logs_list_format(self) -> list:
        """
        Getter method that returns syslog list.
        """
        return self._logs_list_format

    @logs_list_format.setter
    def logs_list_format(self, list_logs: list) -> None:
        """
        Setter method that changes syslog list.
        """
        self._logs_list_format = list_logs
    
    def build_logs_list_format(self) -> list:
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

    def print_logs(self) -> None:
        """
        Print log data without format.
        """
        self.logs_list_format = self.build_logs_list_format()
        print(self)

    def filter_logs(self, **kwargs) -> None:
        """
        Filtering logs by Date, User and Source.
            Date: date0 - date1, date0, time0 - time1 date0
        """
        logs = []
        for key, value in kwargs.items():
            if key == 'pid':
                logs = [log for log in self.logs_list_format if value in log['source']]
        if logs:
            self.logs_list_format = logs
            print(self)
        else:
            print("There is no search results.")

    def filter_date():
        pass
