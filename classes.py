import os
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
    def __init__(self, hinges, locks, engraving):
        super().__init__()
        self.hinges = hinges
        self.locks = locks
        self.engraving = engraving

    def create_folders(self):
        os.chdir(DOCJOB)
        for engr in self.engraving:
            if engr.group:
                if not os.path.exists(engr.group):
                    os.mkdir(engr.group)
                os.chdir(engr.group)
            if not os.path.exists(engr.name):
                os.mkdir(engr.name)
            os.chdir(engr.name)
            for lock in self.locks:
                if not os.path.exists(lock.name):
                    os.mkdir(lock.name)
                os.chdir(lock.name)
                for hinge in self.hinges:
                    if not os.path.exists(hinge.name):
                        os.mkdir(hinge.name)
                    os.chdir(hinge.name)
                    with open(f"{engr.name}_{lock.name}_{hinge.name}.xxl", "w") as f:
                        self.gcode = self.header
                        f.write(self.gcode)
                    os.chdir("..")
                os.chdir("..")
            os.chdir(DOCJOB)