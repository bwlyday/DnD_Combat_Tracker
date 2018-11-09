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

    new = Combatant(command[1], int(hp) , int(ac), int(init))
    tracker.insert_combatant(new)

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
        subject.change_init(command[2])
        tracker.remove_combatant(subject)
        tracker.insert_combatant(subject)

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

        tracker.report()
        line = input()