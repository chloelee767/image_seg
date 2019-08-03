from pathlib import Path
def set_default_config(filename_no_py):
    currdir = Path(Path(__file__).parent)
    with open(currdir/'default.py','w+') as f:
        f.write(f'from .{filename_no_py} import *')
