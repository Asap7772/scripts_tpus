import os
import subprocess
from collections import OrderedDict

zones = OrderedDict()

zones['europe-west4-a'] = {
    'tpu-{}-a': [0, 2, 3, 9]
}

print("# TOTAL ZONES: {}".format(len(zones)))


blacklist_ips=[]

ips = []
i = 0
print('# GCP TPUs')
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
            print(f'Host ssltpu{i}')
            print(f'  HostName {ip}')
            print(f'  User anikaitsingh')
            print()
            i += 1
            

print("# TOTAL MACHINES: {}".format(i))