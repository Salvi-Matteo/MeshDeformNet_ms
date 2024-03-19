import subprocess

subprocess.call([
    "python", "prediction_gcn.py",
    "--image", "/mnt/c/Users/MatteoSalvi-Medicssr/Desktop/test_prediction",
    "--mesh_dat", "data/template/data_aux.dat",
    "--mesh_txt", "data/template/mesh_info_ct.txt", "data/template/mesh_info_mr.txt",
    "--attr", "_train",
    "--mesh_tmplt", "data/template/init3.vtk",
    "--model", "weights/weights_gcn.hdf5",
    "--output", "/mnt/c/Users/MatteoSalvi-Medicssr/Desktop/test_prediction/output",
    "--modality", "ct",
    "--seg_id", "1", "2", "3", "4", "5", "6", "7",
    "--size", "128", "128", "128",
    "--mode", "test"
])
