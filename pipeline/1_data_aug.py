import subprocess

subprocess.call([   
    "/home/sagemaker-user/.conda/envs/myenv/bin/python3",    "data/data_augmentation.py",
    "--im_dir",    "/home/sagemaker-user/Dataset/ct_train/ct_train",
    "--seg_dir",    "/home/sagemaker-user/Dataset/ct_train/ct_train_seg",
    "--out_dir",    "/home/sagemaker-user/Dataset_aug",
    "--modality",    "ct",
    "--mode",    "train",
    "--num",    "2"
])


