import subprocess

subprocess.call([   
    "python",    "data/data_augmentation.py",
    "--im_dir",    "/mnt/c/Users/MatteoSalvi-Medicssr/Desktop/Model Testing (paper)/ReTraining/mr_train/mr_train",
    "--seg_dir",    "/mnt/c/Users/MatteoSalvi-Medicssr/Desktop/Model Testing (paper)/ReTraining/mr_train/mr_train_seg",
    "--out_dir",    "/mnt/c/Users/MatteoSalvi-Medicssr/Desktop/Model Testing (paper)/ReTraining/mr_train/mr_train_aug",
    "--modality",    "mr",
    "--mode",    "train",
    "--num",    "2"
])

