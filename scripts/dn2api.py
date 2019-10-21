#!/usr/bin/env python3

import requests
import yaml
from pprint import pprint

path_to_dn = (
    "/home/ubuntu/projects/atc-api/tests/files/"
    "DN_0003_1_windows_sysmon_process_creation.yml"
)

with open(path_to_dn, 'r') as stream:
    dn = yaml.safe_load(stream)

# pprint(dn)

r = requests.post(
    'http://127.0.0.1:8000/api/v1/atc/dataneeded/',
    json=dn
)
pprint(r.text)
