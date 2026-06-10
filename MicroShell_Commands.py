import os

def mshell_set(args):
    # string var stuff
    if args[0] == "--str":
        if len(args) < 3:
            print("Error: mShell: MissingStr: You tried to make a string variable but didn't actually attach a string.")
            return
        elif len(args) < 2:
            print("Error: mShell: MissedArgs: Not enough arguments; the structure for the set --str command is \"set --str [variable name] [string]\". [0x06]")
        name = args[1]
        value = " ".join(args[2:])
        vars[name] = value
    # num var stuff
    else:
        if len(args) < 2:
            print("Error: mShell: MissedArgs: Not enough arguments; the structure for the set command is \"set [variable name] [number]\". [0x03]")
            return
        name = args[0]
        try:
            value = int(args[1])
        except ValueError:
            print("Error: mShell: ValueError: Value must be a number [0x04]")
            return
        vars[name] = value

def mshell_print(args):
    if len(args) < 2:
        print('Error: mShell: MissedArgs: Structure is "print [--str/--var] [content]" [0x05]')
        return
    mode = args[0]
    if mode == "--var":
        name = args[1]
        if name in vars:
            print(f"{name} = {vars[name]}")
        else:
            print("Error: mShell: MissingVar: Variable doesn't exist [0x15]")
    elif mode == "--str":
        print(" ".join(args[1:]))
    else:
        print('Error: mShell: FlagError: Invalid flag; you should check out "exit" for some help on the structure of commands [0x16]')


def mshell_del(args):
    name = args[0]
    if name in vars:
        del vars[name]
    else:
        print("Error: mShell: NoSuchVar: That variable doesn't exist; There is nothing to delete. [0x07]")

def mshell_listvars(args):
    print(vars)
def mshell_kill(args):
    print("mShell: Who are you planning to kill if there's literally no one, mate?")

def mshell_help(args):
    print("""
Commands:
set (--str) [var] [num] - adds a variable or edits an existing one
print [--str]/[--var] [str]/[var] - prints a variable or plain text
del [var] - delete a variable

help - exits the program
exit - shows help
exitmath - shows math help
""")

def mshell_helpmath(args):
    print("""
Math Commands:
add [var] [num] - add a number to a variable
sub [var] [num] - subtract a number from a variable
mul [var] [num] - multiply a variable by a number
div [var] [num] - divide a variable by a number

addvars [var1] [var2] (resultVar) - add two variables together
subvars [var1] [var2] (resultVar) - subtract two variables
mulvars [var1] [var2] (resultVar) - multiply two variables
divvars [var1] [var2] (resultVar) - divide two variables

note:
- if (resultVar) is not provided, var1 is overwritten
- math only works with numbers
""")
def mshell_exit(args):
    exit()
def mshell_clear(args):
    os.system("cls" if os.name == "nt" else "clear")
    print("""___  ____                _____ _          _ _ 
|  \\/  (_)              /  ___| |        | | |
| .  . |_  ___ _ __ ___ \\ `--.| |__   ___| | |
| |\\/| | |/ __| '__/ _ \\ `--. \\ '_ \\ / _ \\ | |
| |  | | | (__| | | (_) /\\__/ / | | |  __/ | |
\\_|  |_/_|\\___|_|  \\___/\\____/|_| |_|\\___|_|_| 
              "exit" for help                           
""")
def mshell_socrates(args):
    print("Socrates: mShell: If making a small programming language on Python is your power, who are you without it? [0xSOCRATES]")

# the logic for the script command is in MicroShell.py
vars = {
    # It's pretty lonely in here.
    # I wish someone added a variable.
    "friend": "hi friend",
    # Wtf, that actually worked?
    # Huh. That's sure pretty neat.

    # I wish for a million dollars.
    # ...
    # ..........
    # Huh. I see.
    # It's not like I wanted a million dollars or anything.
    "big_money": 1000000
    # Whoa.
}

################ DO NOT FUCKING LOOK FARTHER THAN THIS COMMENT THERE IS SO MUCH SHIT HERE ITS INSANE ################
################ ONLY PROCEED TO SCROLL IF YOU WANT TO SEE OR MODIFY THE COMMAND DICTIONARY. BEWARE. ################

# Addition
def mshell_addvars(args):
    if len(args) < 2:
        print("Error: mShell: MissedArgs: Missing arguments; the structure for the addvars command is \"addvars [var1] [var2] (resultVar)\" [0x08]")
        return

    var1 = args[0]
    var2 = args[1]

    if var1 not in vars or var2 not in vars:
        print("Error: mShell: MissedVar: one or both variables don't exist [0x09]")
        return

    try:
        v1 = int(vars[var1])
        v2 = int(vars[var2])
    except ValueError:
        print("Error: mShell: TypeError: addvars only works with numbers [0x10]")
        return

    result = v1 + v2

    # optional output variable
    if len(args) >= 3:
        out = args[2]
        vars[out] = result
    else:
        vars[var1] = result

def mshell_add(args):
    if len(args) < 2:
        print("Error: mShell: MissedArgs: Not enough arguments; the structure for the add command is \"add [var] [number]\" [0x11]")
        return

    name = args[0]

    # make sure variable exists
    if name not in vars:
        print("Error: mShell: MissingVar: Variable doesn't exist [0x12]")
        return

    try:
        value = int(args[1])
    except ValueError:
        print("Error: mShell: ValueError: The second argument must be a number [0x13]")
        return

    vars[name] += value


# Subtraction
def mshell_subvars(args):
    if len(args) < 2:
        print("Error: mShell: MissedArgs: Missing arguments; the structure for the addvars command is \"subvars [var1] [var2] (resultVar)\" [0x14]")
        return

    var1 = args[0]
    var2 = args[1]

    if var1 not in vars or var2 not in vars:
        print("Error: mShell: MissedVar: one or both variables don't exist [0x09]")
        return

    try:
        v1 = int(vars[var1])
        v2 = int(vars[var2])
    except ValueError:
        print("Error: mShell: TypeError: subvars only works with numbers [0x10]")
        return

    result = v1 - v2

    # optional output variable
    if len(args) >= 3:
        out = args[2]
        vars[out] = result
    else:
        vars[var1] = result

def mshell_sub(args):
    if len(args) < 2:
        print("Error: mShell: MissedArgs: Not enough arguments; the structure for the sub command is \"sub [var] [number]\" [0x17]")
        return

    name = args[0]

    # make sure variable exists
    if name not in vars:
        print("Error: mShell: MissingVar: Variable doesn't exist [0x12]")
        return

    try:
        value = int(args[1])
    except ValueError:
        print("Error: mShell: ValueError: The second argument must be a number [0x13]")
        return

    vars[name] -= value


# Multiplication
def mshell_mulvars(args):
    if len(args) < 2:
        print("Error: mShell: MissedArgs: Missing arguments; the structure for the mulvars command is \"mulvars [var1] [var2] (resultVar)\" [0x20]")
        return

    var1 = args[0]
    var2 = args[1]

    if var1 not in vars or var2 not in vars:
        print("Error: mShell: MissedVar: one or both variables don't exist [0x09]")
        return

    try:
        v1 = int(vars[var1])
        v2 = int(vars[var2])
    except ValueError:
        print("Error: mShell: TypeError: addvars only works with numbers [0x10]")
        return

    result = v1 * v2

    # optional output variable
    if len(args) >= 3:
        out = args[2]
        vars[out] = result
    else:
        vars[var1] = result

def mshell_mul(args):
    if len(args) < 2:
        print("Error: mShell: MissedArgs: Not enough arguments; the structure for the mul command is \"mul [var] [number]\" [0x23]")
        return

    name = args[0]

    # make sure variable exists
    if name not in vars:
        print("Error: mShell: MissingVar: Variable doesn't exist [0x12]")
        return

    try:
        value = int(args[1])
    except ValueError:
        print("Error: mShell: ValueError: The second argument must be a number [0x13]")
        return

    vars[name] *= value


# Division
def mshell_divvars(args):
    if len(args) < 2:
        print("Error: mShell: MissedArgs: Missing arguments; the structure for the divvars command is \"divvars [var1] [var2] (resultVar)\" [0x20]")
        return

    var1 = args[0]
    var2 = args[1]

    if var1 not in vars or var2 not in vars:
        print("Error: mShell: MissedVar: one or both variables don't exist [0x09]")
        return

    try:
        v1 = int(vars[var1])
        v2 = int(vars[var2])
    except ValueError:
        print("Error: mShell: TypeError: divvars only works with numbers [0x10]")
        return

    result = v1 / v2

    # optional output variable
    if len(args) >= 3:
        out = args[2]
        vars[out] = result
    else:
        vars[var1] = result

def mshell_div(args):
    if len(args) < 2:
        print("Error: mShell: MissedArgs: Not enough arguments; the structure for the div command is \"div [var] [number]\" [0x23]")
        return

    name = args[0]

    # make sure variable exists
    if name not in vars:
        print("Error: mShell: MissingVar: Variable doesn't exist [0x12]")
        return

    try:
        value = int(args[1])
    except ValueError:
        print("Error: mShell: ValueError: The second argument must be a number [0x13]")
        return

    vars[name] /= value



############################## THIS IS WHERE THE COMMANDS ARE ###################################
############################## THIS IS WHERE THE COMMANDS ARE ###################################
############################## THIS IS WHERE THE COMMANDS ARE ###################################
############################## THIS IS WHERE THE COMMANDS ARE ###################################


mShell_cmds = {
    # Main 3
    "set": mshell_set,
    "print": mshell_print,
    "del": mshell_del,
    # Math
    "add": mshell_add,
    "addvars": mshell_addvars,
    "sub": mshell_sub,
    "subvars": mshell_subvars,
    "mul": mshell_mul,
    "mulvars": mshell_mulvars,
    "div": mshell_div,
    "divvars": mshell_divvars,
    # Funny Useless Shit
    "socrates": mshell_socrates,
    "kill": mshell_kill,
    # Help & Exit & other stuff ig
    "help": mshell_exit,
    "exitmath": mshell_helpmath,
    "exit": mshell_help,
    "clear": mshell_clear,
    "listvars": mshell_listvars
}
