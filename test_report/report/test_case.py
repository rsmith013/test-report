# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '15 Jan 2021'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'


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




