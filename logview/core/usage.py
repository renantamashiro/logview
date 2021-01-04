from importlib import import_module


USAGE = """Linux log view

Usage: log-view [OPTIONS] COMMAND [ARGS]

Options:
"""


class Usage:
    def __init__(self, version):
        self._version = version
        self._options = list()

    def version(self):
        """
        Return version.
        """
        print(f"Linux log view, version {self._version}")

    def add_option(self, cmd: str, option: str,
                   description: str, fn=None) -> None:
        """
        Add options to usage menu.
        """
        opt = ((cmd, option, description), {'fn': fn})
        self._options.append(opt)
    
    def view_usage(self):
        """
        Visualize usage menu.
        """
        sorted_options = sorted(self._options)
        options_string = []
        for line in sorted_options:
            cmd, option, description = line[0]
            options_string.append(f"   {cmd.ljust(6)}{option.ljust(14)}{description}\n")
        print(USAGE + ''.join(options_string), end='')

    def run_option(self, option, *args, **kwargs):
        """
        Run a specific option.
        """
        for line in self._options:
            if option in line[0]:
                func = line[1]['fn']
                break
        log_view = import_module('core.log_view')
        try:
            getattr(log_view, func)(*args, **kwargs)
        except TypeError as e:
            if option == '-h' or option == '--help':
                self.view_usage()
            else:
                self.version()
