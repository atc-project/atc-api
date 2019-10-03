import requests
import yaml
import os

def export_some_entity(url, val, entity_key="id"):
    to_send = {entity_key: val}
    r = requests.post(url, data=to_send)
    return r.json()[entity_key]

def export_dn(path_to_dn):
    with open(path_to_dn, 'r') as stream:
        try:
            dn = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            raise

    for key in ('category', 'platform', ('log_type', 'type'), 'channel', 'provider'):
        if isinstance(key, tuple):
            dn[key[0]] = {"name": dn[key[1]]}
        else:
            dn[key] = {"name": dn[key]}
    arr = []
    for field in dn['fields']:
        arr.append({"name":field})
    dn['log_field'] = arr
    arr = []
    for ref in dn['references']:
        arr.append({"url": ref})
    dn['reference'] = arr
    dn['logging_policy'] = dn.pop('loggingpolicy')
    arr=[]
    r = requests.post('http://127.0.0.1:8000/api/v0/atc/dataneeded/', json=dn)
    print(r)




if __name__=='__main__':
    path = 'atomic-threat-coverage/data_needed'
    for file in os.listdir(path):
        export_dn(f'{path}/{file}')


