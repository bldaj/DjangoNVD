import re
import json
from datetime import datetime


def read_cve_json_file(filename):
    with open(filename) as f:
        return json.load(f)


def get_current_year():
    return datetime.now().year


def get_year_from_filename(filename: str):
    return re.findall(r'(\d+)', filename)
