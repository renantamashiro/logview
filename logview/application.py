import sys

from core.usage import Usage


def build() -> Usage:
    """
    Add commands and options for an Usage instance.
    """
    usage = Usage('0.0.0')
    usage.add_option('-h', '--help', 'Show this message and exit.', None)
    usage.add_option('-v', '--version', 'Show the version and exit.', None)
    usage.add_option('-f', '--filter', 'Filter option.', 'filter_logs')
    usage.add_option('-p', '--print', 'Print all logs.', 'print_all')
    usage.add_option('-s', '--sort', 'Print all logs.', 'sorting')
    return usage

def run(option=None, args=[], kwargs={}) -> None:
    """
    Run logview.
    """
    try: 
        usage = build()
        if len(option) > 2:
            args_list = list(option[2:])
            args = [args_list.pop(i) for i in range(len(args_list)) if args_list[i].find("=") == -1]
            kwargs = dict([arg.split("=") for arg in args_list]) if args_list else {}
        usage.run_option(option[1], *args, **kwargs)
    except IndexError:
        print(usage.view_usage(), end='')
