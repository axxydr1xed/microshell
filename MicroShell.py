from time import sleep as slp
import os, socket
import MicroShell_Commands as ms

def mshell_script(args):
    if len(args) < 2:
        print("Error: mShell: MissedArgs: Not enough arguments; the structure for the script command is \"script [new/mod/run] [name].msh\". [0x03]")
        return
    mode = args[0]
    name = args[1]

    if mode == "new":
        if not name.endswith(".msh"):
            print("Error: mShell: BadFileExt: the correct extension for MicroShell files is .msh")
            return
        with open(name, "w") as f:
            f.write("# MicroShell script")
        print(f"Created file: {name}")
    elif mode == "run":
        if not name.endswith(".msh"):
            print("Error: mShell: BadFileExt: use .msh")
            return

        try:
            with open(name, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("Error: mShell: NoFile: script not found")
            return

        for line in lines:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split()
            cmd = parts[0]
            args = parts[1:]
            commands[cmd](args)

        commands["script"] = lambda args: mshell_script(args)
    elif mode == "mod":
        print("Placeholder: mShell: this is a placeholder™")
    else:
        print("Error: mShell: BadMode: That isn't a mode for the script command; are you sure it's new, mod or run?")

commands = ms.mShell_cmds
hostname = socket.gethostname()
commands["script"] = mshell_script
print("  hello, world! welcome to microshell :)  ")
slp(0.5)
print("this is a simple math programming language")
slp(1)
print("built for use right from your command line")
slp(0.5)
print("\n      type \"exit\" for a help message      ")
slp(2)
os.system("cls" if os.name == "nt" else "clear")
print("""___  ____                _____ _          _ _ 
|  \\/  (_)              /  ___| |        | | |
| .  . |_  ___ _ __ ___ \\ `--.| |__   ___| | |
| |\\/| | |/ __| '__/ _ \\ `--. \\ '_ \\ / _ \\ | |
| |  | | | (__| | | (_) /\\__/ / | | |  __/ | |
\\_|  |_/_|\\___|_|  \\___/\\____/|_| |_|\\___|_|_| 
              "exit" for help                           
""")

while True:
    line = input(f"mShell@{hostname} # > ")
    parts = line.split()
    if not parts:
        print("Error: mShell: NoCommand: No command added; try actually typing something next time [0x01]")
        continue

    cmd = parts[0]
    args = parts[1:]
    if cmd in commands:
        commands[cmd](args)
    else:
        print("Error: mShell: MissingCmd: Command not found; are you sure that's a real command? [0x02]")