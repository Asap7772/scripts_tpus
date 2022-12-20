# Script Tpu
This is a repository for useful scripts for using TPUs from GCP. The scripts are based on the [TPU tutorial](https://cloud.google.com/tpu/docs/tutorials/mnist) from Google Cloud. I have added some scripts to make it easier to use the TPU:
- `make_tpu_config`: Creates a ssh configuration file for the TPUs.
- `create_tpu.sh`: Creates a TPU instance by querying the GCP API.
- `copy_path.sh`: Copies a folder from the TPU to local directories.
- `install_conda.py`: Installs conda on the TPU.


## Collecting Speech Data
To setup TPU config, run the following command:
```
python make_tpu_config.py --user $USER > tmp_file.txt
```

## Making a TPU
To split the collected data into subsets, run the following command:
```
python create_tpus.py --zone us-central1-a --version tpu-vm-base --accelerator_type v3-8
```