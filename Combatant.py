
class Combatant:

    def __init__(self, name, hp, ac, initiative):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.initiative = initiative

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, heal):
        self.hp += heal

    def get_hp(self):
        return self.hp

    def get_initiative(self):
        return self.initiative

    def get_ac(self):
        return self.ac

    def change_ac(self, new_ac):
        self.ac = new_ac

    def change_init(self, new_init):
        self.initiative = new_init

    def __repr__(self):
        string = ""
        if len(self.name) <5:
            string = "{}\t\tHP: {} AC: {} Initiative: {}".format(self.name, self.hp, self.ac, self.initiative)
        else:
            string = "{}\tHP: {} AC: {} Initiative: {}".format(self.name, self.hp, self.ac, self.initiative)
        return string