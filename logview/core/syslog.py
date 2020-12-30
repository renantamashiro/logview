class Syslog:
    def __init__(self, log):
        self._log = log
        self._log_dict = self.build_log_dict()
        self._log_print = self.formatted(self.log_dict)
    
    @property
    def log(self):
        """
        Getter method that returns syslog without format.
        """
        return self._log
    
    @log.setter
    def log(self, log):
        """
        Setter method that changes syslog data.
        """
        self._log = log
    
    @property
    def log_dict(self):
        """
        Getter method that returns syslog dict.
        """
        return self._log_dict

    @property
    def log_print(self):
        """
        Getter method that returns syslog print.
        """
        return self._log_print
    
    @log_print.setter
    def log_print(self, logs):
        """
        Setter method that change log print data.
        """
        self._log_print = logs

    def no_format(self):
        """
        Print syslog without format.
        """
        print(self._log)
    
    def build_log_dict(self):
        """
        Returns a list of dicts organized by date, user, source, and event.
        """
        data = self.log
        log_dict = list()
        for line in data.split("\n"):
            try:
                date = line[:15]
                event_loc = line[16:].find(":") + 16
                user, source = line[16:event_loc].split(" ")
                event = line[event_loc+1:]
                log_dict.append({
                    "date": date,
                    "user": user,
                    "source": source,
                    "event": event
                    })
            except ValueError:
                continue
        return log_dict

    def formatted(self, logs: list):
        """
        Print log data formatted.
        """
        print_data = ""
        for line in logs:
            print_data += (f"{line['date'].center(16)}"
                         f"|{line['user'].center(12)}"
                         f"|{line['source'].center(20)}"
                         f"|{line['event']}\n")
        return print_data

    def print_data(self):
        """
        Print log data without format.
        """
        self.log_print = self.formatted(self.log_dict())


    def filter_log(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'pid':
                logs = [log for log in self.log_dict if value in log['source']]
        self.log_print = self.formatted(logs)


class LogStr:
    def __init__(self, log: dict):
        self.date = log['date']
        self.user = log['user']
        self.source = log['source']
        self.event = log['event']
    
    def __str__(self):
        return f"{self.date} {self.user} {self.source} {self.event}"
