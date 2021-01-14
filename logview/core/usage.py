from importlib import import_module


USAGE = """Linux log view

Usage: log-view [OPTIONS] COMMAND [ARGS]

Options:
"""


class Usage:
    def __init__(self, version):
        self._version = version
        self._options = list()

    @property
    def version(self):
        """
        Return version.
        """
        return f"Linux log view, version {self._version}"

    def add_option(self, cmd: str, option: str,
                   description: str, fn=None) -> None:
        """
        Add options to usage menu.
        """
        test_params = (
            isinstance(cmd, str) and
            isinstance(option, str) and
            isinstance(description, str)
        )
        if test_params:
            opt = ((cmd, option, description), {'fn': fn})
            self._options.append(opt)
        else:
            raise TypeError("CMD, Option, Description and Function must be strings")
    
    def view_usage(self):
        """
        Visualize usage menu.
        """
        sorted_options = sorted(self._options)
        options_string = []
        for line in sorted_options:
            cmd, option, description = line[0]
            options_string.append(f"   {cmd.ljust(6)}{option.ljust(14)}{description}\n")
        return USAGE + ''.join(options_string)

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
            print(e)
            if option == '-h' or option == '--help':
                print(self.view_usage(), end='')
            else:
                print(self.version)
