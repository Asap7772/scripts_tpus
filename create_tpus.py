import os
import time

zone='us-central1-a'
version='tpu-vm-base'
accelerator_type='v3-8'

which_tpus = {
    'anikait-tpu-{}-y': list(range(6)),
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