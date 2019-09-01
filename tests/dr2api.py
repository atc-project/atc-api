import requests
import yaml

def export_dr(path_to_dr):
    with open(path_to_dr, 'r') as stream:
        try:
            dr = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            raise


    r = requests.post('http://127.0.0.1:8000/api/v0/atc/detectionrule/', data=dr)
    print(r)




if __name__=='__main__':
    export_dr('files/sysmon_ads_executable.yml')


