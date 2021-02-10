class Extra:
    def __init__(self):
        self.FN = -1  # 0
        self.MW = -1  # 1
        self.FT = -1  # 2
        self.WW = -1  # 3
        self.BS = -1  # 4
        self.SFN = -1  # 5  # cele cu S in fata au StatTrak (valoreaza mai mult)
        self.SMW = -1  # 6
        self.SFT = -1  # 7
        self.SWW = -1  # 8
        self.SBS = -1  # 9


# cele cu S in fata au StatTrak (valoreaza mai mult)
# pentru fiecare calitate stim pretul
class Skin:
    def __init__(self):
        self.extra = Extra()
        self.name = ""
        self.weapon = ""
        self.rarity = ""


# fiecare cutie cu skin-uri + link-ul cu date despre skin-urile din ea
class Case:
    def __init__(self):
        self.name = ""
        self.link = ""
        self.Skins = []
