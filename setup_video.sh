sudo rm -rf /mnt/disks/persist
sudo rm -rf ~/hdd; mkdir ~/hdd; sudo mount /dev/sdb ~/hdd;

sudo rm -rf ~/video_proj_exps;

mkdir ~/hdd/video_proj_exps; cd ~/hdd/video_proj_exps
git clone https://github.com/aviralkumar2907/minibullet.git; cd minibullet; git checkout multi_container_multi_obj_kevin; cd -
git clone https://github.com/ikostrikov/jaxrl2_private.git jaxrl2; cd jaxrl2; git checkout anikait_sarsa_for_v_head_duel_arch; cd -

sudo apt-get install gcc python3-dev python3-setuptools -y
sudo pip3 install --no-cache-dir -U crcmod

mkdir pre-training-data; cd pre-training-data; gsutil -m cp -rn gs://pre-training-data/multiobj_grasp_32_tasks_6k_noise0.15_6400.npy .; cd


wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p ~/hdd/miniconda

conda env create -f ~/jax_tpu.yml

conda activate jax_tpu; pip install gym==0.23.0 moviepy imageio ipdb
/home/anikaitsingh/hdd/miniconda/envs/jax_tpu/bin/pip install gym==0.23.0 moviepy imageio ipdb

pip install --upgrade pip
pip install "jax[tpu]>=0.2.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
