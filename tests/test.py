# -*- coding: UTF-8 -*-
import sys
import unittest

from os.path import dirname

if __name__ == '__main__':
    here = dirname(__file__)
    sys.path.insert(0, here + '/..')

import freesms


class TestVersion(unittest.TestCase):
    def test_version(self):
        self.assertRegexpMatches(freesms.__version__, r'^\d+\.\d+\.\d+')


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover(here)
    t = unittest.TextTestRunner().run(suite)
    if not t.wasSuccessful():
        sys.exit(1)
