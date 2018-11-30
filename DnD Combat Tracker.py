from Tracker import *
from Combatant import *
from Parser import *

no_combatant = "Combatant not found"
# command is a list. The elements should be a string containing the command, then a string containing the name of the subject, then the damage done
# all other commands will follow this or a similar format
def damage(command):
    subject = tracker.find_combatant(command[1])
    if subject == None:
        print(no_combatant)
    else:
        subject.take_damage(command[2])


def heal(command):
    subject = tracker.find_combatant(command[1])
    if subject == None:
        print(no_combatant)
    else:
        subject.heal(command[2])


def remove(command):
    subject = tracker.find_combatant(command[1])
    if subject == None:
        print(no_combatant)
    else:
        tracker.remove_combatant(subject)

def add(command):
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

    init = input("Place in Initiative List: ")
    while init.isdigit() == False:
        print("Please input a valid place.")
        init = input("Place: ")
    init = int(init)

    new = Combatant(command[1], max_hp, hp, ac, 0) #TODO add meaningful initiative instead of 0
    tracker.insert_combatant(init, new)

def change_ac(command):
    subject = tracker.find_combatant(command[1])
    if subject == None:
        print(no_combatant)
    else:
        subject.change_ac(command[2])

def change_init(command):
    subject = tracker.find_combatant(command[1])
    if subject == None:
        print(no_combatant)
    else:
        # subject.change_init(command[2])
        tracker.remove_combatant(subject)
        tracker.insert_combatant(command[2], subject)

def help():
    print(Parser.__help__)

if __name__ == '__main__':
    #start the tracker
    tracker = Tracker()
    tracker.add_combatants()
    #tracker.add_test_combatants()
    tracker.report()

    line = input()
    while(line.lower() != "quit"):
        command = parse_line(line)
        if command == None:
            pass
        elif command[0] == Parser.help:
            help()
        elif command[0] == Parser.damage:
            damage(command)
        elif command[0] == Parser.heal:
            heal(command)
        elif command[0] == Parser.change_ac:
            change_ac(command)
        elif command[0] == Parser.change_init:
            change_init(command)
        elif command[0] == Parser.remove:
            remove(command)
        elif command[0] == Parser.add:
            add(command)
        elif command[0] == Parser.next:
            tracker.take_turn()
        elif command[0] == Parser.back:
            tracker.back()

        tracker.report()
        line = input()