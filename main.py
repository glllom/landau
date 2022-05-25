import os

JOB = r"C:\Program Files\SCM Group\Xilog Plus\Job\\"


class Program:
    def __init(self):
        self.header = ""
        self.gcode = ""


class Lock(Program):
    def __init__(self, name):
        super().__init__()
        self.height = ""
        self.path = JOB + r"templates\Lock\\" + name


lock_magnet = Lock("Lock_magnet")
Lock_AGB_EN12209 = Lock("Lock_AGB_EN12209")


class Hinge(Program):
    def __init__(self, name):
        super().__init__()
        self.height = ""
        self.path = JOB + r"templates\Hinges\\" + name


hinge_cemom = Lock("Hinge_Cemom-80")
hinge_luz = Lock("Hinge_LUZ")


class Engraving(Program):
    def __init__(self, name):
        super().__init__()
        self.path = JOB + r"templates\Engraving\\" + name


n1 = Engraving("N1")
n2 = Engraving("N2")
n3 = Engraving("N3")


class Door(Program):
    def __init__(self, hinges, locks, engraving):
        super().__init__()
        self.hinges = hinges
        self.locks = locks
        self.engraving = engraving


    def create_folders(self):
        os.mkdir(JOB)


door_landau = Door(hinges=[hinge_cemom, hinge_luz], locks=[lock_magnet, Lock_AGB_EN12209], engraving=[n1, n2, n3])
