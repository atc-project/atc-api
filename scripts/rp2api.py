#!/usr/bin/env python3

import requests
import yaml
from pprint import pprint
from os import walk

import getpass
uinput = input(
    "[?] Provide a username [" + getpass.getuser() +"]: "
)
uinput = uinput or getpass.getuser()
upassw = getpass.getpass("[?] Provide a password: ")
print("[+] Got credentials -> " + uinput + ":" + "*" * len(upassw))

# path_to_ra = (
#     "/home/ubuntu/projects/atc-api/tests/files/"
#     "RA_0001_identification_get_original_email.yml"
# )

rp_dir = '/home/ubuntu/projects/atomic-threat-coverage/response_playbooks'

dirpath, _, filenames = next(walk(rp_dir))

for file in filenames:
    if file[-4:] != ".yml":
        continue
    with open(dirpath + "/" + file, 'r') as stream:
        rp = yaml.safe_load(stream)

    r = requests.post(
        'http://127.0.0.1:8000/api/v1/atc/responseplaybook/',
        json=rp, auth=(uinput, upassw)
    )

    if r.status_code // 100 != 2:
        pprint(file)
        pprint(r.text)

# pprint(r.text)
