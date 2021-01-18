# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '15 Jan 2021'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

from functools import wraps
from test_report.report import TestResults


def test_results(func):
    """
    :return:
    """
    @wraps(func)
    def wrapper(*args):
        test_results = TestResults(func.__name__, item=args[0].item)
        return func(*args, results=test_results)
    return wrapper