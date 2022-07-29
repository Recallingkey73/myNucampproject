class Player():
    def __init__(self):
        self.hp = (100, 1000)
        self.attk = (25, 75)

class KnightClass(Player):
    def __init__(self):
        super().__init__()
        self.hp = 1000
        self.attk = 50

class WizardClass(Player):
    def __init__(self):
        super().__init__()
        self.hp = 500
        self.attk = 75

class ArcherClass(Player):
    def __init__(self):
        super().__init__()
        self.hp = 750
        self.attk = 50

class RougeClass(Player):
    def __init__(self):
        super().__init__()
        self.hp = 300
        self.attk = 25


knight = KnightClass()
wizard = WizardClass()
archer = ArcherClass()
rouge = RougeClass()