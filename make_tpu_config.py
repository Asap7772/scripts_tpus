import os
import subprocess
import argparse
from collections import OrderedDict

argparser = argparse.ArgumentParser()
argparser.add_argument('--user', type=str, default='anikaitsingh')
args = argparser.parse_args()

zones = OrderedDict()

zones['us-central1-a'] = {
    'aviral-tpu-{}' : [4, 5, 11, 19, 21, 22],
    'bridge-tpu-{}' : [6, 9],
    'anikait-tpu-{}-x': [8,10],
    'anikait-tpu-{}-y': [],
}

print("# TOTAL ZONES: {}".format(len(zones)))


blacklist_ips=[]

ips = []
i = 0
for zone in zones:
    print('# ZONE = {}'.format(zone))
    for prefix in zones[zone]:
        for which_tpu in zones[zone][prefix]:
            tpu_name = prefix.format(which_tpu)
            command = f'gcloud alpha compute tpus tpu-vm describe {tpu_name} --zone {zone}'
            result = subprocess.run(command.split(), stdout=subprocess.PIPE)       
            full_str = result.stdout.decode('utf-8')            
            
            ip = full_str.split('externalIp:')[1].split('ipAddress:')[0].strip()
            
            ips.append(ip)
            additional_str = 'blacklist' if ip in blacklist_ips else ''
            print(f'# {tpu_name} = {ip} {additional_str}')
            print(f'Host atpu{i}')
            print(f'  HostName {ip}')
            print(f'  User {args.user}')
            print()
            i += 1
            

print("# TOTAL MACHINES: {}".format(i))