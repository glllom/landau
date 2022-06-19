import os
from file_operations import convert, create_folder, JOB


DOCJOB = "C:\Program Files\SCM Group\Xilog Plus\Job\\"


class Program:
    def __init__(self):
        self.gcode = ""


class Lock(Program):
    def __init__(self, name, short_name):
        super().__init__()
        self.height = ""
        self.name = name
        self.short_name = short_name
        self.path = JOB + "templates\Locks" + chr(92) + name
        self.gcode = f'XS X=DX-1000 Y=0 Z=0 N="{self.path}"  test=test IF=DY<=858\n'
        self.gcode_opposite = f'XS X=DX-1000+correctionDX Y=0 Z=0 N="{self.path}_F5"  test=test IF=DY>858\n'


class Hinge(Program):
    def __init__(self, name, short_name, amount=2, symmetry=True):
        super().__init__()
        self.symmetry = symmetry
        self.amount = amount
        self.name = name
        self.short_name = short_name
        self.path = JOB + "templates\Hinges" + chr(92) + name

    def get_code(self, amount, direction='0'):
        return f'XS X=0 Y=0 Z=0 N="{self.path}" amount={amount} direction={direction}\n'


class Engraving(Program):
    def __init__(self, name, group=None):
        super().__init__()
        self.name = name
        self.group = group
        self.path = f"{JOB}Templates{chr(92)}Engraving{chr(92)}{self.group + chr(92) if self.group else ''}{name}.pgm"
        self.header = 'H DX=2020 DY=740 DZ=43 -A C=0 T=0 R=100 *MM /"def.tlg"\n'
        self.parameters = 'PAR flipped=0\n'
        self.end = 'XN X=3350\n'

    def get_code(self, flipped=0, test=1):
        return f'XS X=0 Y=0 Z=0 N="{self.path}"  flipped={flipped} test={test}\n'

    def create_files(self):
        os.chdir(DOCJOB)
        create_folder('9.רכיבים')
        create_folder('3.חריטות')
        if self.group:
            create_folder(self.group)
        filename = f"{self.name}.xxl"
        with open(filename, "w") as f:
            self.gcode += self.header
            self.gcode += self.parameters
            self.gcode += self.get_code("flipped")
            self.gcode += self.end
            f.write(self.gcode)
        convert(filename)


class Door(Program):
    def __init__(self, hinges, locks, engraving, add_parts, root, dx='2020', dy='730', dz='42.5'):
        super().__init__()
        self.hinges = hinges
        self.locks = locks
        self.engraving = engraving
        self.add_parts = add_parts
        self.root = root
        self.header = f'H DX={dx} DY={dy} DZ={dz} -AD C=0 T=0 R=100 *MM /"def.tlg"\n'
        self.param = 'PARSECTION /"Additional"\nPAR originalDX " "\nPAR sh =5 " "\n'
        self.gcode_checkDX = 'IF NDEF originalDX THEN\nXMSG Q=1# N="----> OriginDX !!! <----"\nFI\n'
        self.boring = 'IF DEF originalDX THEN\nL correctionDX =DX-originalDX\nREF DX=originalDX\nFI\nXS X=0 Y=0 Z=0' \
                      ' N="C:\PROGRAM FILES\SCM GROUP\XILOG PLUS\JOB\TEMPLATES\OTHERS\Boring_for_paint.pgm"\n'
        self.chamfer = 'XS X=sh Y=0 Z=0 N="C:\PROGRAM FILES\SCM GROUP\XILOG PLUS\JOB\TEMPLATES\OTHERS\CHAMFER"\n'
        self.snd_side = 'XN X=3350\nXMSG N="תכין צד שני"\nSET STANDBY =2\n'
        self.end = 'XN X=3350\n'

    def create_files(self):
        os.chdir(DOCJOB)
        create_folder(self.root)
        for engr in self.engraving:
            if engr.group:
                create_folder(engr.group)
            create_folder(engr.name)
            for lock in self.locks:
                create_folder(lock.short_name)
                for hinge in self.hinges:
                    create_folder(hinge.short_name)
                    for amount in hinge.amount:  # different amount
                        if hinge.symmetry:
                            filename = f"{engr.name}_{lock.short_name}__{amount}-{hinge.short_name}.xxl"
                            with open(filename, "w") as f:
                                self.gcode = self.header
                                self.gcode += self.param
                                if self.locks is not []:
                                    self.gcode += lock.gcode
                                if self.hinges is not []:
                                    self.gcode += hinge.get_code(amount)
                                self.gcode += self.boring
                                if "chamfer" in self.add_parts:
                                    self.gcode += self.chamfer
                                if self.engraving is not []:
                                    self.gcode += engr.get_code(1)
                                if self.engraving is not [] or "chamfer" in self.add_parts:
                                    self.gcode += self.snd_side
                                    self.gcode += lock.gcode_opposite
                                    if self.engraving is not []:
                                        self.gcode += engr.get_code(2, 0)
                                    if "chamfer" in self.add_parts:
                                        self.gcode += self.chamfer
                                self.gcode += self.end
                                f.write(self.gcode)
                            convert(filename)
                        else:
                            for (index, direction) in [(1, 'R'), (2, 'L')]:
                                filename = f"{engr.name}_{lock.short_name}__{amount}-{hinge.short_name}-{direction}.xxl"
                                with open(filename, "w") as f:

                                    self.gcode = self.header
                                    self.gcode += self.param
                                    if self.locks is not []:
                                        self.gcode += lock.gcode
                                    if self.hinges is not []:
                                        self.gcode += hinge.get_code(
                                            amount, index)
                                    self.gcode += self.boring
                                    if "chamfer" in self.add_parts:
                                        self.gcode += self.chamfer
                                    if self.engraving is not []:
                                        self.gcode += engr.get_code(flipped=1)
                                    if self.engraving is not [] or "chamfer" in self.add_parts:
                                        self.gcode += self.snd_side
                                        self.gcode += lock.gcode_opposite
                                        if self.engraving is not []:
                                            self.gcode += engr.get_code(
                                                flipped=2, test=0)

                                        if "chamfer" in self.add_parts:
                                            self.gcode += self.chamfer
                                    self.gcode += self.end
                                    f.write(self.gcode)
                                convert(filename)

                    os.chdir("..")
                os.chdir("..")
            os.chdir(DOCJOB)
            os.chdir(self.root)

    def create_files_wo_engr(self):
        os.chdir(DOCJOB)
        create_folder(self.root)
        create_folder("N00")
        for lock in self.locks:
            create_folder(lock.short_name)
            for hinge in self.hinges:
                create_folder(hinge.short_name)
                for amount in hinge.amount:  # different amount
                    if hinge.symmetry:
                        filename = f"N00_{lock.short_name}_{amount}-{hinge.short_name}.xxl"
                        with open(filename, "w") as f:
                            self.gcode = self.header
                            self.gcode += self.param
                            if self.locks is not []:
                                self.gcode += lock.gcode
                            if self.hinges is not []:
                                self.gcode += hinge.get_code(amount)
                            self.gcode += self.boring
                            if "chamfer" in self.add_parts:
                                self.gcode += self.chamfer
                                self.gcode += self.snd_side
                                self.gcode += lock.gcode_opposite
                                self.gcode += self.chamfer
                            self.gcode += self.end
                            f.write(self.gcode)
                        convert(filename)
                    else:
                        for (index, direction) in [(1, 'R'), (2, 'L')]:
                            filename = f"N00_{lock.short_name}_{amount}-{hinge.short_name}-{direction}.xxl"
                            with open(filename, "w") as f:

                                self.gcode = self.header
                                self.gcode += self.param
                                if self.locks is not []:
                                    self.gcode += lock.gcode
                                if self.hinges is not []:
                                    self.gcode += hinge.get_code(amount, index)
                                self.gcode += self.boring
                                if "chamfer" in self.add_parts:
                                    self.gcode += self.chamfer
                                    self.gcode += self.snd_side
                                    self.gcode += lock.gcode_opposite
                                    self.gcode += self.chamfer
                                self.gcode += self.end
                                f.write(self.gcode)
                            convert(filename)

                os.chdir("..")
            os.chdir("..")
        os.chdir(DOCJOB)
        os.chdir(self.root)


class SlidingDoor(Door):
    def __init__(self, locks, engraving, add_parts, root, dx='2020', dy='730', dz='42.5'):
        super().__init__()
        self.locks = locks
        self.engraving = engraving
        self.add_parts = add_parts
        self.root = root
        self.header = f'H DX={dx} DY={dy} DZ={dz} -AD C=0 T=0 R=100 *MM /"def.tlg"\n'
        self.param = 'PARSECTION /"Additional"\nPAR originalDX " "\nPAR sh =5 " "\n'
        self.gcode_checkDX = 'IF NDEF originalDX THEN\nXMSG Q=1# N="----> OriginDX !!! <----"\nFI\n'
        self.boring = 'IF DEF originalDX THEN\nL correctionDX =DX-originalDX\nREF DX=originalDX\nFI\nXS X=0 Y=0 Z=0' \
                      ' N="C:\PROGRAM FILES\SCM GROUP\XILOG PLUS\JOB\TEMPLATES\OTHERS\Boring_for_paint.pgm"\n'
        self.chamfer = 'XS X=sh Y=0 Z=0 N="C:\PROGRAM FILES\SCM GROUP\XILOG PLUS\JOB\TEMPLATES\OTHERS\CHAMFER"\n'
        self.snd_side = 'XN X=3350\nXMSG N="תכין צד שני"\nSET STANDBY =2\n'
        self.end = 'XN X=3350\n'


class Felz(Door):
    def __init__(self, locks, hinges, engraving, root, dx='2020', dy='730', dz='42.5'):
        super().__init__(locks, hinges, engraving, False, root)
        self.locks = locks
        self.hinges = hinges
        self.engraving = engraving
        self.root = root
        self.header = f'H DX={dx} DY={dy} DZ={dz} -AD C=0 T=0 R=100 *MM /"def.tlg"\n'
        self.param = 'PARSECTION /"Additional"\nL felz =DZ-27\n'
        self.snd_side = 'XN X=3350\nXMSG N="תכין צד שני"\nSET STANDBY =2\n'
        self.end = 'XN X=3350\n'

    def create_files(self):
        os.chdir(JOB)
        create_folder(self.root)
        for engr in self.engraving:
            if engr.group:
                create_folder(engr.group)
            create_folder(engr.name)
            for lock in self.locks:
                create_folder(lock.short_name)
                for hinge in self.hinges:
                    create_folder(hinge.short_name)
                    for amount in hinge.amount: 
                        for (index, direction) in [(1, 'R'), (2, 'L')]:
                            filename = f"{engr.name}_{lock.short_name}__{amount}-{hinge.short_name}-{direction}.xxl"
                            #print(filename)
                            with open(filename, "w") as f:
                                self.gcode = self.header
                                self.gcode += self.param
                                self.gcode += lock.get_code(index)
                                self.gcode += hinge.get_code(amount, index)
                                self.gcode += f'XS X=0 Y=0 Z=0 N="C:\PROGRAM FILES\SCM GROUP\XILOG PLUS\JOB\TEMPLATES\OTHERS\REBATE" Direction={index}\n'
                                self.gcode += self.chamfer
                                self.gcode += engr.get_code(flipped=1)
                                self.gcode += self.snd_side
                                self.gcode += lock.gcode_opposite
                                self.gcode += engr.get_code(flipped=2, test=0)
                                self.gcode += self.chamfer
                                self.gcode += self.end
                                f.write(self.gcode)
                            convert(filename)
            os.chdir("..")
            os.chdir("..")
            os.chdir(JOB)
            os.chdir(self.root)
