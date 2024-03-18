
import subprocess

subprocess.call([
    "python",    "train_gcn.py",
    "--im_train",   "/content/drive/MyDrive/Processed Images",
    "--im_val",    "/content/drive/MyDrive/Processed Images",
    "--mesh_txt",    "data/template/mesh_info_ct.txt",    "data/template/mesh_info_mr.txt",
    "--mesh",    "data/template/data_aux.dat",
    "--attr_trains",    "",
    "--attr_vals",    "",
    "--train_data_weights",    "1.",
    "--val_data_weights",    "1.",
    "--output",    "/content/drive/MyDrive/Model_saved",
    "--modality",    "ct",    "mr",
    "--num_epoch",    "500",
    "--batch_size",   "1",
    "--lr",    "0.001",
    "--size",    "128",    "128",    "128",
    "--weights",    "0.29336324",    "0.05",    "0.46902252",    "0.16859047",
    "--mesh_ids",    "0",    "1",    "2",    "3",    "4",    "5",    "6",
    "--num_seg",    "1",
    "--seg_weight",    "100."
])