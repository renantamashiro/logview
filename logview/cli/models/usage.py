import inspect

from importlib import import_module


USAGE = """Linux log view

Usage: log-view COMMAND [OPTION] [ARGS]

COMMANDS:
"""

usage_options = [
    "option_accessors",
]


def option_description(name: str, cmd: str, help_usage_message: str) -> None:
    """
    A decorator that set basic attributes
    for each command (`name`, `cmd`, `help message`)
    """

    def function_option(fn):
        def option_accessors(*args, **kwargs):
            if "help" in args:
                return help_usage_message
            elif "cmd" in args:
                return cmd
            elif "name" in args:
                return name
            else:
                fn(*args, **kwargs)

        return option_accessors

    return function_option


def general_help_message_builder(*args):
    """
    Attributes to extract:
        - __name__
        -
    """
    help_string = ""
    for cls_option in args:
        methods = inspect.getmembers(cls_option, predicate=inspect.isfunction)
        for method in methods:
            if method[1].__name__ in usage_options:
                name = getattr(cls_option, method[0])("name")
                cmd = getattr(cls_option, method[0])("cmd")
                help_msg = getattr(cls_option, method[0])("help")
    pass


class UsageCreator:
    """
    Para cada classe a ser criada
    """

    def __init__(self, cls: object):
        self.cls_instance = cls
        self.command_name = cls.__name__
        self.command_module = cls.__module__
        self.command_options = self.getoptions()

    def getoptions(self) -> list:
        """
        Build a dictionary of commands {'-c', command_function}.
        """
        methods = inspect.getmembers(self.cls_instance, predicate=inspect.isfunction)
        command_options = list()
        for method in methods:
            if method[1].__name__ in usage_options:
                cmd = getattr(self.cls_instance, method[0])("cmd")
                command_options.append((cmd, method[0]))
        return command_options


class Usage:
    """
    Escrever essa classe da seguinte forma:
        Cada módulo de comandos do logview deve importar a classe
        Usage e utilizar o decorator que irei criar

        Assim, na instancia do Usage em application, essa classe
        irá mapear os métodos que possuem o decorator e configurar
        o comando e a sua descrição para exibição no Help.

        Alguns modulos:
            Filtering and Sorting
            Converting (csv, json, excel)
            Database
    """

    def __init__(self, version):
        self._version = version
        self._options = list()

    @property
    def version(self):
        """
        Return version.
        """
        return f"Linux log view, version {self._version}"

    def add_option(self, cmd: str, option: str, description: str, fn=None) -> None:
        """
        Add options to usage menu.
        """
        test_params = (
            isinstance(cmd, str)
            and isinstance(option, str)
            and isinstance(description, str)
        )
        if test_params:
            opt = ((cmd, option, description), {"fn": fn})
            self._options.append(opt)
        else:
            raise TypeError("The parameters must be strings")

    def view_usage(self):
        """
        Visualize usage menu.
        """
        sorted_options = sorted(self._options)
        options_string = []
        for line in sorted_options:
            cmd, option, description = line[0]
            options_string.append(f"   {cmd.ljust(6)}{option.ljust(14)}{description}\n")
        return USAGE + "".join(options_string)

    def run_option(self, option, *args, **kwargs):
        """
        Run a specific option.
        """
        for line in self._options:
            if option in line[0]:
                func = line[1]["fn"]
                break
        logview = import_module("core.logview")
        try:
            getattr(logview, func)(*args, **kwargs)
        except TypeError as e:
            print(e)
            if option == "-h" or option == "--help":
                print(self.view_usage(), end="")
            else:
                print(self.version)
