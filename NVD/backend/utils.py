import json
from datetime import datetime


def read_cve_json_file(filename):
    with open(filename) as f:
        return json.load(f)


def get_current_year():
    return datetime.now().year
