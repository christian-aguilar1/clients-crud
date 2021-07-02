import ntpath
import os
import sys
from pathlib import Path

route = os.path.dirname(__file__)
arr_route = route.split(sep=os.path.sep)
route = Path(route)
for a_dir in reversed(arr_route):
    if a_dir != "src":
        route = route.parent
    else:
        break