from Combatant import *

class Tracker:

    def __init__(self):
        self.combatants = []
        self.com_dict = {}
        self.initiative = []
        self.num_com = 0


    #Used to add the initial combatants. Adds new combatants to end of list. DO NOT USE AFTER COMBAT HAS STARTED.
    def add_combatants(self):
        # ask for num combatants
        num_combatants = input("How many combatants?")
        while num_combatants.isdigit() == False:
            print("Please input a valid number of combatants.")
            num_combatants = input("")
        print("Please enter each combatant's name, HP, AC, and Initiative.")
        for i in range(0, int(num_combatants)):
            name = input("Name:")
            name = name.lower().rstrip().lstrip()
            while " " in name:
                print("Name cannot contain spaces.")
                name = input("Name:")
                name = name.lower().lstrip().rstrip()

            max_hp = input("Max HP: ")
            while max_hp.isdigit() == False:
                print("Please input a valid Max HP.")
                max_hp = input("Max HP: ")
            max_hp = int(max_hp)

            hp = input("Current HP: ")
            while hp.isdigit() == False:
                print("Please input a valid HP.")
                hp = input("HP: ")
            hp = int(hp)

            ac = input("AC: ")
            while ac.isdigit() == False:
                print("Please input a valid ac.")
                ac = input("AC: ")
            ac = int(ac)

            done = False
            while(not done):
                init = input("Initiative: ")
                try:
                    init = float(init)
                    done = True
                except:
                    print("Please input a valid initiative.")

            com = Combatant(name, hp, max_hp, ac, init)
            self.add_to_dict(com) #may append number the end of the name if duplicate names occur
            self.combatants.append(com)
            self.num_com += 1
        self.sort_combatants()


    def add_to_dict(self, to_add):
        temp_name = to_add.name
        i = 2
        while temp_name in self.com_dict:
            temp_name = to_add.name + str(i)
            i+=1
        to_add.name = temp_name
        self.com_dict[temp_name] = to_add


    def add_test_combatants(self):
        odran = Combatant("odran", 50, 50, 16, 14)
        mia = Combatant("mia", 30, 30, 18, 19)
        nike = Combatant("nikephoros", 24, 24, 14, 12)
        self.combatants.append(odran)
        self.combatants.append(mia)
        self.combatants.append(nike)
        self.add_to_dict(odran)
        self.add_to_dict(mia)
        self.add_to_dict(nike)
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


    # used to add combatant after combat has started.
    # inserts a combatant into a designated place in the initiative list
    # If combatants share the same name, a number will be appended to the end e.g. Wolf, Wolf2, Wolf3
    def insert_combatant(self, index, combatant):
        self.add_to_dict(combatant)
        self.combatants.insert(index-1, combatant)
        self.num_com += 1
        # uses index-1 because the list the DM sees does not start at 0
        # i.e. the DM would say say to insert at 1, which is combatants[0], not combatants[1]

    # removes a combatant from the initiative list
    def remove_combatant(self, combatant):
        self.combatants.remove(combatant)
        self.num_com -= 1


    def get_combatant(self, i):
        return self.combatants[i]

    # called by the "next" command
    # advances combat by 1 turn
    def take_turn(self):
        comb = self.combatants[0]
        self.combatants.remove(comb)
        self.combatants.append(comb)

    # called by the "back" command
    # goes back 1 turn in combat
    def back(self):
        comb = self.combatants[self.num_com - 1]
        self.combatants.remove(comb)
        self.combatants.insert(0, comb)

    #prints the current turn order
    def report(self):
        end_line = "-"*100

        print(end_line)
        #print combatant info
        for i in range(1, self.num_com+1):
            print("{}. {}".format((i), self.get_combatant(i-1).__repr__()))
        print(end_line)