export TPU_NAME=anikait-v4-0
export ZONE=us-central2-b
export RUNTIME_VERSION=tpu-vm-v4-pt-1.13
export PROJECT_ID=rail-tpus
export ACCELERATOR_TYPE=v4-8

gcloud compute tpus tpu-vm create ${TPU_NAME} \
--zone us-central2-b \
--accelerator-type ${ACCELERATOR_TYPE} \
--version ${RUNTIME_VERSION} \
--subnetwork=tpusubnet

