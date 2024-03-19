import subprocess

subprocess.call([   
    "python3",    "data/data_augmentation.py",
    "--im_dir",    "/content/drive/MyDrive/Dataset/ct_train/ct_train",
    "--seg_dir",    "/content/drive/MyDrive/Dataset/ct_train/ct_train_seg",
    "--out_dir",    "/content/drive/MyDrive/Dataset_augmented",
    "--modality",    "ct",
    "--mode",    "train",
    "--num",    "2"
])


