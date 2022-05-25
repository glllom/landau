import os
from file_operations import convert, create_folder

JOB = r"C:\Program Files\SCM Group\Xilog Plus\Job\\"
DOCJOB = r"C:\Users\glebo\OneDrive\Documents\landau\job\\"


class Program:
    def __init__(self):
        self.header = 'H DX=2000.00 DY=600.00 DZ=43.00 -A C=0 T=0 R=1 *MM /"def.tlg"'
        self.gcode = ""


class Lock(Program):
    def __init__(self, name):
        super().__init__()
        self.height = ""
        self.name = name
        self.path = JOB + r"templates\Lock\\" + name


class Hinge(Program):
    def __init__(self, name):
        super().__init__()
        self.height = ""
        self.name = name
        self.path = JOB + r"templates\Hinges\\" + name


class Engraving(Program):
    def __init__(self, name, group=None):
        super().__init__()
        self.name = name
        self.path = JOB + r"templates\Engraving\\" + name
        self.group = group


class Door(Program):
    def __init__(self, hinges, locks, engraving, root):
        super().__init__()
        self.hinges = hinges
        self.locks = locks
        self.engraving = engraving
        self.root = root

    def create_files(self):
        os.chdir(DOCJOB)
        create_folder(self.root)
        for engr in self.engraving:
            if engr.group:
                create_folder(engr.group)
            create_folder(engr.name)
            for lock in self.locks:
                create_folder(lock.name)
                for hinge in self.hinges:
                    create_folder(hinge.name)
                    filename = f"{engr.name}_{lock.name}_{hinge.name}.xxl"
                    with open(filename, "w") as f:
                        self.gcode = self.header
                        f.write(self.gcode)
                    convert(filename)
                    os.chdir("..")
                os.chdir("..")
            os.chdir(DOCJOB)
            os.chdir(self.root)
