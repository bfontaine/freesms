import re

import freesms


def test_version():
    assert re.match(r'^\d+\.\d+\.\d+', freesms.__version__)
