import sys

from core.usage import Usage
from core.log_view import filter_pid, print_all


def build() -> Usage:
    """
    Add commands and options for an Usage instance.
    """
    usage = Usage('0.0.0')
    usage.add_option('-h', '--help', 'Show this message and exit.', None)
    usage.add_option('-v', '--version', 'Shoe the version and exit.', None)
    usage.add_option('-f', '--filter', 'Filter option.', 'filter_pid')
    usage.add_option('-p', '--print', 'Print all logs.', 'print_all')
    return usage

def run(option=None, args=[], kwargs={}) -> None:
    """
    Run logview.
    """
    try: 
        usage = build()
        if len(option) > 3:
            args_list = list(option[2:])
            args = [args_list.pop(i) for i in len(args_list-1) if args_list[i].find("=") == -1]
            kwargs = dict([arg.split("=") for arg in args_list])
        usage.run_option(option[1], *args, **kwargs)
    except IndexError:
        usage.view_usage()
