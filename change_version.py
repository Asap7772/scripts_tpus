from cloud_tpu_client import Client
from collections import OrderedDict
import subprocess
zones = OrderedDict()

import os

zones['us-central1-a'] = {
    'aviral-tpu-{}' : [4, 5, 11, 19, 21, 22],
    'bridge-tpu-{}' : [6, 9],
    'anikait-tpu-{}-x': [8,10],
    'anikait-tpu-{}-y': [],
}
target_version='pytorch-1.13'

for zone in zones:
    for prefix in zones[zone]:
        for num in zones['us-central1-a'][prefix]:
            tpu_name = prefix.format(num)
            command = f'gcloud alpha compute tpus tpu-vm describe {tpu_name} --zone {zone}'
            result = subprocess.run(command.split(), stdout=subprocess.PIPE)       
            full_str = result.stdout.decode('utf-8')            
            ip = full_str.split('externalIp:')[1].split('ipAddress:')[0].strip()
            print(tpu_name, ip)
            
            os.system(f"export TPU_NAME={tpu_name}")
            os.system(f"export ZONE=us-central1-a")
            os.system(f"export RUNTIME_VERSION=tpu-vm-v4-pt-1.13")
            os.system(f"export PROJECT_ID=rail-tpus")
            
            c = Client(tpu=tpu_name, zone=zone, project='rail-tpus')
            c.configure_tpu_version(target_version, restart_type='ifNeeded')
            c.wait_for_healthy()