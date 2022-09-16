cd ~/hdd/video_proj_exps; 

cd minibullet; git checkout multi_container_multi_obj_kevin; git pull; /home/anikaitsingh/hdd/miniconda/envs/jax_tpu/bin/python setup.py develop; cd -; 
cd jaxrl2; git checkout anikait_sarsa_for_v_head_duel_arch; git pull; /home/anikaitsingh/hdd/miniconda/envs/jax_tpu/bin/python setup.py develop; cd -

sudo apt-get install gcc python3-dev python3-setuptools -y
sudo pip3 install --no-cache-dir -U crcmod

/home/anikaitsingh/hdd/miniconda/envs/jax_tpu/bin/pip install gym==0.23.0 moviepy imageio ipdb

/home/anikaitsingh/hdd/miniconda/envs/jax_tpu/bin/pip install --upgrade pip
/home/anikaitsingh/hdd/miniconda/envs/jax_tpu/bin/pip install "jax[tpu]>=0.2.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html