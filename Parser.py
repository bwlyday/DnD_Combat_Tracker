# damage            subject damage  number
# heal              subject heal number
# remove combatant  subject remove
# add combatant     subject add
# change ac         subject change ac number
# change initiative subject change initiative number
# next              next
# help              help

class Parser:
    damage = "damage"
    heal = "heal"
    remove = "remove"
    add = "add"
    change = "change"
    change_ac = "change ac"
    change_init = "change initiative"
    help = "help"
    next = "next"

    damage_usage = "Damage command has 2 inputs: name and damage value. For example, damage Nikephoros 10 deals 10 damage to Nikephoros.\n"

    __help__ = "Commands:\ndamage [name] [amount]\nheal [name] [amount]\nremove [name]\nadd [name]\nchange ac [name] [new ac]\nchange initiative [name] [new initiative]\nnext\nquit\n"

def parse_line(line):
    command = get_word(line)
    if command == Parser.help:
        return [command]
    elif command == Parser.damage or command == Parser.heal:
        return command_damage_heal(command, line)
    elif command == Parser.remove or command == Parser.add:
        return command_remove_add(command, line)
    elif command == Parser.change:
        return command_change(command, line)
    elif command == Parser.next:
        return [command]
    print("Unknown Command")
    return [None, None, None]


#returns the first word of a string in lowercase.
def get_word(line):
    i = 0
    lower = line.lower()
    word = ""

    #skip past white space
    while(i < len(line) and lower[i]==' '):
        i+=1

    while (i < len(lower) and lower[i] != ' '):
        word += lower[i]
        i+=1
    return word


def command_damage_heal(command, line):
    subject = get_word(line[len(command):])  # doesn't need +1 because get_word ignores initial white space
    remain = line[len(command) + 1:]  # +1 to account for white space
    remain = remain[len(subject) + 1:]  # +1 to account for white space
    if remain.isdigit():
        amount = int(remain)
    else:
        print("Last argument of {} must be a number".format(command))
        return None
    return [command, subject, amount]


def command_remove_add(command, line):
    subject = get_word(line[len(command):])
    return [command, subject]


def command_change(command, line):
    change = get_word(line[len(command):])
    if (change.lower() != "ac"):
        if (change.lower() != "initiative"):
            print("Unkown command")
            return None
    command += " "
    command += change
    subject = get_word(line[len(command):])  # doesn't need +1 because get_word ignores initial white space
    remain = line[len(command) + 1:]  # +1 to account for white space
    remain = remain[len(subject) + 1:]  # +1 to account for white space
    if remain.isdigit():
        amount = int(remain)
    else:
        print("New {} must be a number".format(change))
        return None
    amount = int(remain)
    return [command, subject, amount]