# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '15 Jan 2021'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

from test_report.display import TextColours
from test_report.exceptions import TestFailureException

class TestCase:

    def __init__(self, verbosity=0, *args, **kwargs):
        self.verbosity = verbosity
        self.failed = False

    def run_test(self, callable):

        # Get the test
        test = getattr(self, callable)

        # Get the results
        results = test()

        # Display the results
        if results.failed or self.verbosity > 0:
            print(results)

            if results.failed:
                self.failed = True

    def setup_class(self):
        pass

    def run(self):

        self.setup_class()

        # Run the tests
        tests = [func for func in dir(self) if func.startswith('test_') and callable(getattr(self, func))]

        for test in tests:
            self.run_test(test)

    @classmethod
    def run_loop(cls, cmd_args):

        TEST_FAILED = False

        # Get list of datasets
        for item in cls.iterator:
            print(f'\n\n{TextColours.BOLD}Testing {item}', end=" ")

            test_class = cls(verbosity=cmd_args.verbose, item=item)
            test_class.run()

            if not test_class.failed:
                print(f'{TextColours.OKGREEN}...OK{TextColours.ENDC}')
            else:
                TEST_FAILED = True
                print()

        return TEST_FAILED

    @classmethod
    def run_tests(cls, args):

        TEST_FAILED = cls.run_loop(args)

        if TEST_FAILED:
            raise TestFailureException



