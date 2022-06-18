from msilib.schema import Directory
import subprocess
import os

JOB = "C:\Program Files\SCM Group\Xilog Plus\Job\\"
ENGRAVING = "C:\Program Files\SCM Group\Xilog Plus\Job\Templates\Engraving\\"

def convert(filename):
    subprocess.run([r"C:\Program Files\SCM Group\Xilog Plus\Bin\Winxiso.exe", filename, "-s"])
    os.remove(filename)


def create_folder(name):
    if not os.path.exists(name):
        os.mkdir(name)
    os.chdir(name)

    
def get_files_dirs(path):
    engrav_list = []
    dirfiles = os.scandir(path)
    for element in dirfiles:
        if os.path.isfile(element):
            engrav_list.append(str(element.name))
        else:
            if element.name != "corners":
                engrav_list.extend(list(map(lambda file: (file, element.name), get_files_dirs(f"{path}{element.name}"))))
    return engrav_list

