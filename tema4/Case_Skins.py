
# pentru fiecare calitate stim pretul
class Skin():
    def __init__(self):
        self.name = ""
        self.weapon = ""
        self.rarity = ""
        self.FN = 0
        self.MW = 0
        self.FT = 0
        self.WW = 0
        self.BS = 0

# fiecare cutie cu skin-uri + link-ul cu date despre skin-urile din ea
class Case():
    def __init__(self):
        self.case_name = ""
        self.link = ""
        self.Skins = []