import subprocess

def install_libraries():
    with open("/content/MeshDeformNet_ms/requirements.txt", "r") as file:
        for line in file:
            package = line.strip()
            subprocess.run(["conda", "install", package], check=True)

if __name__ == "__main__":
    install_libraries()
