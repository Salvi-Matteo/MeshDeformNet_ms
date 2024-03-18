import subprocess

subprocess.call([   
"python",    "data/data2tfrecords.py",
    "--folder",    "/path/to/top/image/directory",
    "--modality",    "ct",    "mr",    
    "--size",    "128",    "128",    "128",
    "--folder_postfix",    "_train",
    "--deci_rate",    "0",
    "--smooth_ite",    "50",
    "--out_folder",    "/path/to/output",
    "--seg_id",    "1",    "2",    "3",    "4",    "5",    "6",    "7"
])