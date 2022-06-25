from classes import Lock, Hinge, Engraving, Door, Felz
from file_operations import get_files_dirs, ENGRAVING

lock_magnet = Lock("Lock_Magnet", "Magnet")
Lock_AGB_EN12209 = Lock("Lock_AGB_EN12209", "AGB")

hinge_cemom = Hinge("Cemom_80.pgm", "צרפתי-80", [2, 3])
hinge_luz = Hinge("LUZ", "LUZ", [2, 3], False)
hinge_folded = Hinge("hinge_folded", "מקופף", [2], False)
hinge_simonswerk340 = Hinge("Simonswerk_340.pgm", "s340", [2, 3])
eng_lst = list(map(lambda elem: Engraving(elem[0], elem[1]) if isinstance(elem, tuple) else Engraving(elem), get_files_dirs(ENGRAVING)))
# eng_lst.extend(Engraving("N00"))

door_landau = Door(hinges=[hinge_cemom, hinge_luz, hinge_simonswerk340],
                   locks=[lock_magnet, Lock_AGB_EN12209],
                   engraving=eng_lst, add_parts=("chamfer"), root="3. דלתות לנדאו")

engraving_only = Door(hinges=[], locks=[], engraving=eng_lst, add_parts=("chamfer"), root="חריטות")
#door_landau.create_files()

# door_felz = Felz(hinges=[hinge_folded], locks=[Lock_AGB_EN12209], engraving=eng_lst, root="2. דלתות ממ''ד")
# door_felz.create_files()
