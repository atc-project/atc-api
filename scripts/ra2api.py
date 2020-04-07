#!/usr/bin/env python3

import requests
import yaml
from pprint import pprint
from os import walk

path_to_ra = (
    "/home/ubuntu/projects/atc-api/tests/files/"
    "RA_0001_identification_get_original_email.yml"
)

ra_dir = '/home/ubuntu/projects/atomic-threat-coverage/response_actions'

dirpath, _, filenames = next(walk(ra_dir))

for file in filenames:

    with open(dirpath + "/" + file, 'r') as stream:
        ra = yaml.safe_load(stream)

    r = requests.post(
        'http://127.0.0.1:8000/api/v1/atc/responseaction/',
        json=ra
    )

    if r.status_code // 100 != 2:
        pprint(file)
        pprint(r.text)

# pprint(r.text)
