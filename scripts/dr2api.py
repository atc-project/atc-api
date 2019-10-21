import requests
import yaml
from atcutils import ATCutils
import os

def export_dr(path_to_dr):

    dr = ATCutils.read_yaml_file(path_to_dr)
    dn = ATCutils.main_dn_calculatoin_func(path_to_dr)
    dr['data_needed_names'] = dn
    r = requests.post('http://127.0.0.1:8000/api/v0/atc/detectionrule/', json=dr)
    print(r)






if __name__=='__main__':
    path = '../detection_rules/sigma/rules/apt/'
    for file in os.listdir(path):
        export_dr(f'{path}/{file}')



