import sys
from pathlib import Path
# `path.parents[1]` is the same as `path.parent.parent`
d = Path(__file__).resolve().parents[0]
src_path = Path.joinpath(d, "src")
sys.path.insert(0,  str(src_path))


from appy.hello import create_app 
app = create_app('settings.cfg')