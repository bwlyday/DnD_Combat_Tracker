
class Combatant:

    def __init__(self, name, max_hp, hp, ac, initiative):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.ac = ac
        self.initiative = initiative

    def take_damage(self, damage):
        if damage <= self.hp:
            self.hp -= damage
        else:
            self.hp = 0

    def heal(self, heal):
        query = ""
        if self.hp + heal > self.max_hp:
            while query != "yes" and query != "no":
                query = input("Add temporary HP? (yes/no)")
                query = query.lower()
                if query == "yes":
                    self.hp += heal
                elif query == "no":
                    self.hp = max(self.max_hp, self.hp)
        else:
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

    def compare(self, other):
        i = 0
        while( i < len(self.initiative) and i < len(other.initiative) and self.initiative[i] == other.initiative[i]):
            i+=1
        return other.initiative[i] - self.initiative[i]

    def __repr__(self):
        string = "{:20s} HP: ({:3d}/{:3d}) AC: {:3d}".format(self.name, self.hp, self.max_hp, self.ac)

        return string