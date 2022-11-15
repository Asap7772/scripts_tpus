path=/home/aviralkumar/hdd/11_14_macaw_metatest_4slot/
output_path="/raid/trainingdata/anikait_exps"
machines=(atpu0 atpu1 atpu2 atpu3 atpu4 atpu5 atpu6 atpu7 atpu8)

for machine in ${machines[@]}; do
    curr_output_path="$output_path/$machine/"
    command="mkdir -p $curr_output_path; rsync -vae ssh $machine:$path $curr_output_path &"
    echo $command
    eval $command
done