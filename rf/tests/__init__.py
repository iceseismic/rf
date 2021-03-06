"""
Tests for the rf package.
"""

from pkg_resources import resource_filename
import sys
import unittest


def run():
    loader = unittest.TestLoader()
    test_dir = resource_filename('rf', 'tests')
    suite = loader.discover(test_dir)
    runner = unittest.runner.TextTestRunner()
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)

if __name__ == '__main__':
    run()