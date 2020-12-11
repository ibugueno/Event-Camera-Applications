#!/bin/bash --login

set -e

source /opt/conda/etc/profile.d/conda.sh

echo $CONDA_PREFIX

# activate conda environment and let the following process take over
conda activate v2e

echo $1
echo $2
echo $3, $4

python v2e.py -i $1 --no_preview --timestamp_resolution=.005 --dvs_exposure duration 0.005 --output_folder=$2 --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --dvs_aedat2 data.aedat --output_width=$3 --output_height=$4
