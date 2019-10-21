import requests
import yaml
import os


def export_lp(path_to_lp):
    with open(path_to_lp, 'r') as stream:
        try:
            lp = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            raise

    ids = []
    for event_id in lp.get('eventID', []):
        to_send = {'id': event_id}
        r = requests.post("http://127.0.0.1:8000/api/v0/atc/eventid/", data=to_send)
        ids.append(r.json()['id'])
    lp['event_id'] = ids

    ids = []
    for ref in lp['references']:
        to_send = {'url': ref}
        r = requests.post("http://127.0.0.1:8000/api/v0/atc/reference/", data=to_send)
        ids.append(r.json()['id'])
    lp['reference'] = ids


    ids = []
    for vol in [lp['volume']]:
        to_send = {'name': vol}
        r = requests.post("http://127.0.0.1:8000/api/v0/atc/volume/", data=to_send)
        ids.append(r.json()['id'])
    lp['volume'] = ids[0]
    lp['config'] = lp.pop('configuration')

    r = requests.post("http://127.0.0.1:8000/api/v0/atc/loggingpolicy/", data=lp)
    print(lp)


if __name__ == '__main__':
    path = 'atomic-threat-coverage/logging_policies'
    for file in os.listdir(path):
        export_lp(f'{path}/{file}')
