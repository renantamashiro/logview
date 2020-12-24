import sys

from usage import Usage


with open('/var/log/syslog', 'r') as data:
    SYSLOG = data.read()

def format_logs(fn):
    def wrapped():
        output_log = fn()
        output_log += 'Eu sou o renan'
        return output_log
    return wrapped    

@format_logs
def filter_pid(filter_option: str):
    pass

@format_logs
def print_all():
    print(SYSLOG)
    return SYSLOG

def build():
    usage = Usage('0.0.0')
    usage.add_option('-h', '--help', 'Show this message and exit.', None)
    usage.add_option('-v', '--version', 'Shoe the version and exit.', None)
    usage.add_option('-f', '--filter', 'Filter option.', 'filter_pid')
    usage.add_option('-p', '--print', 'Print all logs.', 'print_all')
    return usage

def main(option=None, args=[], kwargs={}) -> None:
    try: 
        usage = build()
        if len(option) > 3:
            args_list = list(option[2:])
            args = [args_list.pop(i) for i in len(args_list-1) if args_list[i].find("=") == -1]
            kwargs = dict([arg.split("=") for arg in args_list])
        usage.run_option(option[1], *args, **kwargs)
    except IndexError:
        usage.view_usage()
    
if __name__ == '__main__':
    main(sys.argv)