import os
num_tpus = 8
for i in range(1, num_tpus):
    print('Working on TPU ', i)
    os.system(f'rsync -vae ssh /Users/anikaitsingh/Desktop/scripts/setup_repos.sh atpu{i}:~/')
    os.system(f'ssh atpu{i} "bash setup_repos.sh"')
    # os.system(f'ssh atpu{i} "rm -rf video_proj_exps"')
    # os.system(f'ssh atpu{i} "bash -l ~/setup_video.sh"')
    # os.system(f'ssh atpu{i} "nohup bash ./setup_video.sh > foo.out 2> foo.err < /dev/null &"'n)