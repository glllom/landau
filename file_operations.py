import subprocess
import os


def convert(filename):
    subprocess.run([r"C:\Program Files\SCM Group\Xilog Plus\Bin\Winxiso.exe", filename, "-s"])
    os.remove(filename)


def create_folder(name):
    if not os.path.exists(name):
        os.mkdir(name)
    os.chdir(name)
