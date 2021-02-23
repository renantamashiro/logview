import inspect
from importlib import import_module


usage_options = [
    "option_accessors",
]

usage_menu = """
%s

USAGE
\tlogview [-h] <command> [<arg1>] ... [<argN>]

ARGUMENTS
\t<command>\t\t The command to execute
\t<arg>\t\t\t The arguments of the command

GLOBAL OPTIONS
\t-h (--help)\t\t Display this help message
\t-v (--vesion)\t\t Shows the version of logview

COMMANDS
"""


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


class UsageCreator:
    """
    Para cada classe a ser criada
    """

    def __init__(self, version: str, modules: list):
        self._version = version
        self._modules = modules
        self._command_options = self.getoptions()

    @property
    def version(self):
        """
        Return version.
        """
        return f"Logview version {self._version}"

    def getoptions(self) -> list:
        """
        Build a dictionary of commands {'-c', command_function}.
        """
        command_options = dict()
        for module in self._modules:
            functions = inspect.getmembers(module, predicate=inspect.isfunction)
            for fn in functions:
                if fn[1].__name__ in usage_options:
                    cmd = getattr(module, fn[0])("cmd")
                    command_options[cmd] = (module, fn[0])
        return command_options

    def run_option(self, option, *args, **kwargs):
        """
        Run the command passed by user.
        """
        module, fn = self._command_options[option]
        getattr(module, fn)(*args, **kwargs)

    def help_message(self):
        """
        Attributes to extract:
            - __name__
            -
        """
        print(usage_menu % self.version, end="")
        for cls_option in self._modules:
            methods = inspect.getmembers(cls_option, predicate=inspect.isfunction)
            for method in methods:
                if method[1].__name__ in usage_options:
                    name = getattr(cls_option, method[0])("name")
                    cmd = getattr(cls_option, method[0])("cmd")
                    help_msg = getattr(cls_option, method[0])("help")
                    print(f"\t{cmd} (--{name})\t\t {help_msg}")
