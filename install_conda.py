import os
num_tpus = 14
for i in range(1, num_tpus):
    # os.system(f'ssh atpu{i} "wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh"')
    # os.system(f'ssh atpu{i} "sudo rm -rf ~/hdd; mkdir ~/hdd; sudo mount /dev/sdb ~/hdd; sudo chmod 777 -R ~/hdd/"')
    # os.system(f'ssh atpu{i} "bash ~/miniconda.sh -b -p ~/hdd/miniconda"')
    os.system(f'rsync -vae ssh /Users/anikaitsingh/Desktop/scripts/.bashrc atpu{i}:~/')
    os.system(f'rsync -vae ssh /Users/anikaitsingh/Desktop/scripts/jax_tpu.yml atpu{i}:~/')
    # os.system(f'ssh atpu{i} "conda env create -f ~/jax_tpu.yml"')
    
    
    