command_per_machine="bash /nfs/iris_nfs/users/asap7772/setup_tpu.sh"
ssh_prefix="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
for i in $(seq 1 32); do
    echo "Running command on atpu${i}"
    command='${ssh_prefix} atpu${i} "${command_per_machine}"'
    echo $command
    eval $command
done
echo "Done"