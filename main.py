from os import environ
import sys
from pathlib import Path
# `path.parents[1]` is the same as `path.parent.parent`
d = Path(__file__).resolve().parents[0]
src_path = Path.joinpath(d, "src")
sys.path.insert(0,  str(src_path))


from config import config_dict
from appy import create_app 


get_config_mode = environ.get('APPY_CONFIG_MODE', 'Debug')
try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    sys.exit('Error: Invalid APPY_CONFIG_MODE environment variable entry.')

app = create_app(config_mode)
