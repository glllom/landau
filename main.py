from classes import Lock, Hinge, Engraving, Door
from file_operations import get_files_dirs, ENGRAVING

lock_magnet = Lock("Lock_Magnet", "Magnet")
Lock_AGB_EN12209 = Lock("Lock_AGB_EN12209", "AGB")

hinge_cemom = Hinge("Cemom_80.pgm", "צרפתי-80", [2, 3])
hinge_luz = Hinge("LUZ", "LUZ", [2, 3], False)
hinge_simonswerk340 = Hinge("Simonswerk_340.pgm", "s340", [2, 3])
eng_lst = list(map(lambda elem: Engraving(elem[0], elem[1]) if isinstance(elem, tuple) else Engraving(elem), get_files_dirs(ENGRAVING)))

for eng in eng_lst:
    print(f"Name: {eng.name}, group: {eng.group}")

door_landau = Door(hinges=[hinge_cemom, hinge_luz, hinge_simonswerk340],
                   locks=[lock_magnet, Lock_AGB_EN12209],
                   engraving=eng_lst, add_parts=("chamfer"), root="3. דלתות לנדאו")

engraving_only = Door(hinges=[], locks=[], engraving=eng_lst, add_parts=("chamfer"), root="חריטות")
door_landau.create_files()
door_landau.create_files_wo_engr()
""" creating engraving
for eng in eng_lst:
    eng.create_files() """

