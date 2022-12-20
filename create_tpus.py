import os
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--zone', type=str, default='us-central1-a')
parser.add_argument('--version', type=str, default='tpu-vm-base')
parser.add_argument('--accelerator_type', type=str, default='v3-8')
args = parser.parse_args()

zone=args.zone
version=args.version
accelerator_type=args.accelerator_type

which_tpus = {
    'anikait-tpu-{}-z': list(range(10)),
}

while True:
    for device_type in which_tpus:
        for which_device in which_tpus[device_type]:
            tpu_name = device_type.format(str(which_device)) 
            print('creating {}'.format(tpu_name))
            command = f"gcloud compute tpus tpu-vm create {tpu_name} --zone={zone} --accelerator-type={accelerator_type} --version={version} &"
            print(command)
            os.system(command)

            time.sleep(0.5)
        time.sleep(10)