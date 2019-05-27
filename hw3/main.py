from urls import url_pattern
from web_framework.app import run_server
import sys


if len(sys.argv) == 1:
    print('ERROR: ENTER PORT!')
else:
    port = sys.argv[1]
    run_server(port, url_pattern)
