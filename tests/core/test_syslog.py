import unittest

from logview.core.syslog import Syslog
from logview.core import log_view


class SyslogTest(unittest.TestCase):
    def setUp(self):
        data = log_view.get_logs()
        self.syslog = Syslog(data)
    
    def test_log_setter_getter_methods(self):
        data = log_view.get_logs()
        self.syslog.logs = data
        self.assertEqual(data, self.syslog.logs)
        self.assertIsInstance(self.syslog.logs, list)

    def test_log_setter_getter_methods_malformed_data(self):
        data = ""
        with self.assertRaises(TypeError):
            self.syslog.logs = data

    def test_logs_list_format(self):
        self.assertIsInstance(self.syslog.logs_list_format, list)
        self.assertIsInstance(self.syslog.logs_list_format[0], dict)

    def test_logs_list_format_malformed_data(self):
        data = ""
        with self.assertRaises(TypeError):
            self.syslog.logs_list_format = data

    def test_build_logs_list_format(self):
        self.assertIsInstance(self.syslog.build_logs_list_format(), list)
        self.assertIsInstance(self.syslog.build_logs_list_format()[0], dict)