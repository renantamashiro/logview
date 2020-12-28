class Syslog:
    def __init__(self, log):
        self._log = log
        self._log_dict = self.build_log_dict()
        self._log_print = self.formatted()
    
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

    def formatted(self):
        print_data = ""
        for line in self._log_dict:
            print_data += (f"{line['date'].center(16)}"
                         f"|{line['user'].center(12)}"
                         f"|{line['source'].center(20)}"
                         f"|{line['event']}\n")
        return print_data

    def print_data(self):
        print(self._log_print)
