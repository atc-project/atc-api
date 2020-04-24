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


lp_dir = '/home/ubuntu/projects/atomic-threat-coverage/data_needed'

dirpath, _, filenames = next(walk(lp_dir))

for file in filenames:

    with open(dirpath + "/" + file, 'r') as stream:
        dn = yaml.safe_load(stream)

    r = requests.post(
        'http://127.0.0.1:8000/api/v1/atc/dataneeded/',
        json=dn, auth=(uinput, upassw)
    )

    if r.status_code // 100 != 2:
        pprint(file)
        pprint(r.text)

# pprint(r.text)
