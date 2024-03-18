import subprocess

subprocess.call([  
    "python", "data/data2tfrecords.py", "--folder" ,"/content/drive/MyDrive/Dataset/ct_val",
    "--modality", "ct",
    "--size" ,"128" ,"128", "128" , # image dimension for training
    "--folder_postfix" ,"_val", # _train or _val, i.e. will process the images/segmentation in ct_train and ct_train_seg
    "--deci_rate" ,"0" , # decimation rate on ground truth surface meshes
    "--smooth_ite","50" , # Laplacian smoothing on ground truth surface meshes
    "--out_folder" , "/content/drive/MyDrive/Processed_dataset" ,
    "--seg_id", "1" ,"2", "3" ,"4", "5" ,"6" ,"7" # segmentation ids, 1-7 for seven cardiac structures
])
