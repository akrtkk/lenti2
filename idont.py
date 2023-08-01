import os.path
import sys

def print_in_program(command):
    if command.startswith('printF:'):
        message = command[7:]
        print(message)
    elif command.startswith('while True:'):
        command = command[11:]
        if command.startswith('printF:'):
            message = command[7:]
            while True:
                print(message)
        else:
            print("Invaild while run: {}".replace("{}", command))
    else:
        print("Invalid command format.")

if len(sys.argv) < 2:
    print("Please provide the external file name as an argument.")
    sys.exit(1)

external_file = sys.argv[1]

if os.path.isfile(external_file) and external_file.endswith('.txt'):
    with open(external_file, "r") as f:
        for line in f:
            print_in_program(line.strip())
else:
    print(f"Invalid filename: {external_file}")