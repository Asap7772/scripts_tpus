import os
import time

which_tpus = {
    'aviral-tpu-' : [4, 5, 11, 12, 17, 19, 21, 22],
    'bridge-tpu-' : [6, 8, 9, 10]
}

while True:
    for device_type in which_tpus:
        for which_device in which_tpus[device_type]:
            tpu_name = device_type + str(which_device)

            command = f'gcloud alpha compute tpus tpu-vm start {tpu_name} --zone us-central1-a &'
            print(command)
            os.system(command)

            time.sleep(0.1)
        time.sleep(1)