import os
import time

zones=['europe-west4-a', 'europe-west4-b']
version='tpu-vm-base'
accelerator_type='v3-8'

which_tpus = {
    'tpu-{}-a': (list(range(10)), 0),
    # 'tpu-{}-b': (list(range(10)), 1),
}

while True:
    for device_type in which_tpus:
        lst, zone_i = which_tpus[device_type]
        zone = zones[zone_i]
        for which_device in lst:
            tpu_name = device_type.format(str(which_device)) 
            print('creating {}'.format(tpu_name))
            command = f"gcloud compute tpus tpu-vm create {tpu_name} --zone={zone} --accelerator-type={accelerator_type} --version={version} &"
            print(command)
            os.system(command)

            time.sleep(2)
        time.sleep(20)