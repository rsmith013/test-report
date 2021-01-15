
# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '15 Jan 2021'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

from io import StringIO
from test_report.display import TextColours

class TestResults:

    @property
    def errors(self):
        return len(self.get_errors())

    @property
    def failed(self):
        return bool(self.errors)

    @property
    def warnings(self):
        return len(self.get_warnings())

    def __init__(self, name):
        self.name = name
        self.REPORT = {}

    def __repr__(self):

        with StringIO('') as report:
            report.write(f'\n\t{TextColours.BOLD}TEST: {self.name}')
            if not self.errors:
                report.write(f'{TextColours.OKGREEN} ...OK')

            else:
                report.write(f'\n\n\t\t{TextColours.BOLD}{TextColours.FAIL}ERRORS: {self.errors}')
                report.write(f'\n\t\t{TextColours.BOLD}{TextColours.FAIL}---------')

                for error in self.get_errors():
                    report.write(f'\n\t\t{TextColours.FAIL}{error}')

            if self.warnings:
                report.write(f'{TextColours.BOLD}{TextColours.WARNING}\n\n\t\tWARNINGS: {self.warnings}')
                report.write(f'{TextColours.BOLD}{TextColours.WARNING}\n\t\t---------')

                for warning in self.get_warnings():
                    report.write(f'{TextColours.BOLD}{TextColours.WARNING}\n\t\t{warning}')

            report.write(TextColours.ENDC)
            content = report.getvalue()

        return content

    def add_error(self, message):
        """
        Add an error to the test report
        :param message: Message to add
        """
        if 'error' in self.REPORT:
            self.REPORT['errors'].append(message)
        else:
            self.REPORT['errors'] = [message]

    def add_warning(self, message):
        """
        Add a warning to the test report
        :param message: Message to add
        """

        if 'warning' in self.REPORT:
            self.REPORT['warnings'].append(message)
        else:
            self.REPORT['warnings'] = [message]

    def get_errors(self):
        """
        Return the list of errors
        :return:
        """
        return self.REPORT.get('errors',[])

    def get_warnings(self):
        """
        Return the list of warnings
        :return:
        """
        return self.REPORT.get('warnings',[])