from classes import Lock, Hinge, Engraving, Door

lock_magnet = Lock("Lock_Magnet", "מגנט")
Lock_AGB_EN12209 = Lock("Lock_AGB_EN12209", "AGB")

hinge_cemom = Hinge("Cemom_80.pgm", "צרפתי-80", [2, 3])
hinge_luz = Hinge("LUZ", "LUZ", [2, 3], False)
hinge_simonswerk340 = Hinge("Simonswerk_340.pgm", "s340", [2, 3])
eng_lst = [Engraving("N01_1P20mm", "N01_P20mm"),
           Engraving("N01_2P20mm", "N01_P20mm"),
           Engraving("N02_1P_imm", "N02_P_imm"),
           Engraving("N02_2P_imm", "N02_P_imm"),
           Engraving("N03_1P_ger", "N03_P_ger"),
           Engraving("N03_2P_ger", "N03_P_ger"),
           Engraving("N05_1P_gm6mm", "N05_P_gm6mm"),
           Engraving("N05_2P_gm6mm", "N05_P_gm6mm"),
           Engraving("N07_1P_gm12mm", "N07_P_gm12mm"),
           Engraving("N07_2P_gm12mm", "N07_P_gm12mm"),
           Engraving("N07_3P_gm12mm", "N07_P_gm12mm"),
           Engraving("N14_1P_8mm", "N14_P_8mm"),
           Engraving("N14_2P_8mm", "N14_P_8mm"),
           Engraving("N14_2Ph_8mm", "N14_P_8mm"),
           Engraving("N21_v400"),
           Engraving("N22_v14248"),
           Engraving("N23_v401050"),
           Engraving("N24_"),
           Engraving("N25_v6050148"),
           Engraving("N26_v145060"),
           Engraving("N27_v2323"),
           Engraving("N28_v1423"),
           Engraving("N29_"),
           ]

door_landau = Door(hinges=[hinge_cemom, hinge_luz, hinge_simonswerk340],
                   locks=[lock_magnet, Lock_AGB_EN12209],
                   engraving=eng_lst, add_parts=("chamfer"), root="3.דלתות לנדאו")
door_landau.create_files()
