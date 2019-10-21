#!/usr/bin/env python3

import requests
import yaml
from pprint import pprint

path_to_lp = (
    "/home/ubuntu/projects/atc-api/tests/files/"
    "EN_0001_cache_sysmon_event_id_1_info.yml"
)

with open(path_to_lp, 'r') as stream:
    lp = yaml.safe_load(stream)

r = requests.post(
    'http://127.0.0.1:8000/api/v1/atc/enrichment/',
    json=lp
)

pprint(r.text)

path_to_lp = (
    "/home/ubuntu/projects/atc-api/tests/files/"
    "EN_0002_enrich_sysmon_event_id_1_with_parent_info.yml"
)

with open(path_to_lp, 'r') as stream:
    lp = yaml.safe_load(stream)

r = requests.post(
    'http://127.0.0.1:8000/api/v1/atc/enrichment/',
    json=lp
)

pprint(r.text)
