from classes import Lock, Hinge, Engraving, Door

lock_magnet = Lock("Lock_Magnet")
Lock_AGB_EN12209 = Lock("Lock_AGB_EN12209")

hinge_cemom = Hinge("Hinge_Cemom-80")
hinge_luz = Hinge("Hinge_LUZ")
hinge_simonswerk240 = Hinge("Hinge_s240")
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
           Engraving("N21_123123123"),
           Engraving("N22_123123123"),
           Engraving("N23_123123123"),
           ]

door_landau = Door(hinges=[hinge_cemom, hinge_luz, hinge_simonswerk240], locks=[lock_magnet, Lock_AGB_EN12209],
                   engraving=eng_lst)
door_landau.create_folders()
