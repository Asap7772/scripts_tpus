import os
import subprocess
from collections import OrderedDict

zones = OrderedDict()

# zones['europe-west4-a'] = {
#     'aviral-tpu-' : [2],
# }

zones['us-central1-a'] = {
    'aviral-tpu-{}' : [4, 5, 11, 12, 19, 21, 22],
    'bridge-tpu-{}' : [6, 8, 9],
    'anikait-tpu-{}-x': [15, 5, 8, 9],
}

blacklist_ips=['34.121.100.226', '35.184.95.239', '35.188.144.21', '104.154.76.58', '34.172.77.127']

ips = []
i = 0
for zone in zones:
    print('# ZONE = {}'.format(zone))
    for prefix in zones[zone]:
        for which_tpu in zones[zone][prefix]:
            tpu_name = prefix.format(which_tpu)
            command = f'gcloud alpha compute tpus tpu-vm describe {tpu_name} --zone {zone}'
            result = subprocess.run(command.split(), stdout=subprocess.PIPE)       
            
            ip = result.stdout.decode('utf-8').split('externalIp:')[1].split('ipAddress:')[0].strip()
            if ip in blacklist_ips:
                continue
            
            ips.append(ip)
            
            print(f'Host atpu{i}')
            print(f'  HostName {ip}')
            print(f'  User anikaitsingh')
            print()
            print(f'Host tpu{i}')
            print(f'  HostName {ip}')
            print(f'  User aviralkumar')
            print()
            i += 1
            

print('# NUM TPUS = {}'.format(i))