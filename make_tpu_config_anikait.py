import os
import subprocess
from collections import OrderedDict

zones = OrderedDict()

zones['us-central1-a'] = {
    'anikait-tpu-' : [10, 11, 12, 14, 15, 5, 8, 9],
}

ips = []
i = 0
for zone in zones:
    # print('ZONE = {}'.format(zone))
    for prefix in zones[zone]:
        for which_tpu in zones[zone][prefix]:
            tpu_name = prefix + str(which_tpu)
            command = f'gcloud alpha compute tpus tpu-vm describe {tpu_name}-x --zone {zone}'
            result = subprocess.run(command.split(), stdout=subprocess.PIPE)       
            
            ip = result.stdout.decode('utf-8').split('externalIp:')[1].split('ipAddress:')[0].strip()
            ips.append(ip)
            
            print(f'Host anikait_tpu{i}')
            print(f'  HostName {ip}')
            print(f'  User anikaitsingh')
            print()

            i += 1
            

print('# NUM TPUS = {}'.format(i))