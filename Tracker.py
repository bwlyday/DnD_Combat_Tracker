from Combatant import *

class Tracker:

    def __init__(self):
        self.combatants = []
        self.ally = []
        self.enemy = []
        self.initiative = []
        self.num_com = 0


    #Used to add the initial combatants. Adds new combatants to end of list. DO NOT USE AFTER COMBAT HAS STARTED.
    def add_combatants(self):
        # ask for num allies, then add that many allies
        num_combatants = input("How many combatants?")
        while num_combatants.isdigit() == False:
            print("Please input a valid number of combatants.")
            num_combatants = input("")
        print("Please enter each ally's name, HP, AC, and Initiative.")
        for i in range(0, int(num_combatants)):
            name = input("Name:")
            hp = input("HP: ")
            while hp.isdigit() == False:
                print("Please input a valid HP.")
                hp = input("HP: ")
            ac = input("AC: ")
            while ac.isdigit() == False:
                print("Please input a valid ac.")
                ac = input("AC: ")
            init = input("Initiative: ")
            while init.isdigit() == False:
                print("Please input a valid initiative.")
                init = input("AC: ")
            hp = int(hp)
            ac = int(ac)
            init = int(init)
            self.combatants.append(Combatant(name, hp, ac, init))
            self.num_com += 1
        self.sort_combatants()

    def add_test_combatants(self):
        self.combatants.append(Combatant("Odran", 50,16,14))
        self.combatants.append(Combatant("Mia", 30, 18, 19))
        self.combatants.append(Combatant("Nikephoros", 24, 14, 12))
        self.num_com = 3
        self.sort_combatants()

    def find_combatant(self, name):
        lower = name.lower()
        for i in range(0, self.num_com):
            lower_name = self.combatants[i].name.lower()
            if lower_name == lower:
                return self.combatants[i]
        return None

    #sorts combatants based on initiative
    def sort_combatants(self):
        self.combatants.sort(reverse=True, key=Combatant.get_initiative)


    #used to add combatant after combat has started. If combatants share the same name, a number will be appended to the end e.g. Wolf 1, Wolf 2, Wolf3
    def insert_combatant(self, combatant):
        i = 0
        #find place in list
        while(i < self.num_com and combatant.get_initiative() < self.combatants[i].get_initiative()):
            i+=1

        #add to list
        if(i==self.num_com):
            self.combatants.append(combatant)
        else:
            self.combatants.insert(i, combatant)
        self.num_com+=1


    def remove_combatant(self, combatant):
        self.combatants.remove(combatant)
        self.num_com -= 1


    def get_combatant(self, i):
        return self.combatants[i]


    def take_turn(self):
        comb = self.combatants[0]
        self.combatants.remove(comb)
        self.combatants.append(comb)


    #prints the current turn order
    def report(self):
        end_line = ""
        for i in range(0, 100):
            end_line += "-"

        print(end_line)
        #print combatant info
        for i in range(1, self.num_com+1):
            print("{}. {}".format((i), self.get_combatant(i-1).__repr__()))
        print(end_line)