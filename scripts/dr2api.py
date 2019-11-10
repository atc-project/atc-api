import requests
import yaml

path_to_dr = (
    "/home/ubuntu/projects/atc-api/tests/files/"
    "ADS.yml"
)

with open(path_to_dr, 'r') as f:
    data = [x for x in yaml.safe_load_all(f)]
data = {'raw_rule': data}
r = requests.post('http://127.0.0.1:8000/api/v1/atc/detectionrule/', json=data)
print(r.text)
