from __future__ import (absolute_import, division, print_function, unicode_literals)
try:
    # python 2.x版本
    from urllib import urlopen
except ImportError:
    # python 3.x版本
    from urllib.request import urlopen

import json


json_url = ''