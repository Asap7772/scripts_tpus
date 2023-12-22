import os
import subprocess
import argparse
from collections import OrderedDict

argparser = argparse.ArgumentParser()
argparser.add_argument('--user', type=str, default='anikaitsingh')
args = argparser.parse_args()

zones = OrderedDict()

zones['us-central2-b'] = {
    'iris-v4-vm-{}' : list(range(1, 33)),
}
zones['europe-west4-a'] = {
    'node-{}': list(range(1, 6)),
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
            
            try:
                ip = full_str.split('externalIp:')[1].split('ipAddress:')[0].strip()
            except:
                i += 1
                continue
            i += 1

            ips.append(ip)
            additional_str = 'blacklist' if ip in blacklist_ips else ''
            print(f'# {tpu_name} = {ip} {additional_str}')
            print(f'Host atpu{i}')
            print(f'  HostName {ip}')
            print(f'  User {args.user}')
            print()

print("# TOTAL MACHINES: {}".format(i))