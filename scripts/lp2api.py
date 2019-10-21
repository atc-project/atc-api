#!/usr/bin/env python3

import requests
import yaml
from pprint import pprint

path_to_lp = (
    "/home/ubuntu/projects/atc-api/tests/files/"
    "LP_0003_windows_sysmon_process_creation.yml"
)

with open(path_to_lp, 'r') as stream:
    lp = yaml.safe_load(stream)

r = requests.post(
    'http://127.0.0.1:8000/api/v1/atc/loggingpolicy/',
    json=lp
)

pprint(r.text)
