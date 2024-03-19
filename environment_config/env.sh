#!/bin/bash

wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh
chmod +x Miniconda3-py38_4.12.0-Linux-x86_64.sh
./Miniconda3-py38_4.12.0-Linux-x86_64.sh -b -f -p /usr/local
conda update conda --yes
conda create -n myenv python=3.6 --yes
dpkg -i /content/MeshDeformNet_ms/Env_config/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
sudo apt-get update
sudo apt-get install cuda-toolkit-10-0
sudo dpkg -i /content/MeshDeformNet_ms/Env_config/libcudnn7-doc_7.4.2.24-1+cuda10.0_amd64.deb
sudo apt-get update
