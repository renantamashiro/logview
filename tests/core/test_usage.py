import unittest

from logview.core.usage import Usage


class UsageTest(unittest.TestCase):
    def setUp(self):
        self.usage = Usage("0.0.1")

    def test_add_wront_type_option(self):
        with self.assertRaises(TypeError):
            self.usage.add_option(123, 123, 123, 123)

    def test_run_option(self):
        self.usage.add_option("-c", "--coption", "optionC", "c")
        self.usage.add_option("-b", "--boption", "optionB", "b")
        self.usage.add_option("-a", "--aoption", "optionA", "a")
