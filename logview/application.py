import sys

from cli.filter import Filter
from usagebuilder.usage import UsageCreator


commands = [
    Filter
]


def run():
    options = sys.argv
    usage = UsageCreator("0.0.0", commands)
    try:
        if len(options) > 2:
            args_list = list(options[2:])
            args = [
                args_list.pop(i)
                for i in range(len(args_list))
                if args_list[i].find("=") == -1
            ]
            if args_list:
                kwargs = dict([arg.split("=") for arg in args_list])
        usage.run_option(options[1], *args, **kwargs)
    except IndexError as e:
        usage.help_message()
