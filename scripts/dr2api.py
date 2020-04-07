#!/usr/bin/env python3

import requests
import yaml
from pprint import pprint
from os import walk

dr_dir = (
    '/home/ubuntu/projects/atomic-threat-coverage/detection_rules/sigma/'
    'rules'
)

for dirpath, _, filenames in walk(dr_dir):

    for file in filenames:
        if file[-3:] != "yml":
            continue

        with open(dirpath + "/" + file, 'r') as stream:
            dr = [x for x in yaml.safe_load_all(stream)]
            data = {'raw_rule': dr}

        r = requests.post(
            'http://127.0.0.1:8000/api/v1/atc/detectionrule/',
            json=data
        )

        if r.status_code // 100 != 2:
            # pprint(r.text)
            pprint(file)
