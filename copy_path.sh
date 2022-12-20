path_folder=/home/aviralkumar/hdd/
exps=( "12_20_dualq_proportion" "12_18_dueling_proportion_experiment")

output_path="/raid/trainingdata/anikait_exps"
machines=(atpu0 atpu1 atpu2 atpu3 atpu4 atpu5 atpu6 atpu7 atpu8)
# machines=(atpu9)

for machine in ${machines[@]}; do
    for exp in "${exps[@]}"; do
        curr_output_path="$output_path/$machine/"
        full_path="$path_folder/$exp"

        echo "Copying $full_path to $curr_output_path"
        
        command="mkdir -p $curr_output_path; rsync -vae ssh $machine:$full_path $curr_output_path &"
        echo $command
        eval $command
    done
done