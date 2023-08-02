import os.path
import sys

# Global dictionary to store variables
variables = {}

def print_in_program(command):
    global variables

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
            sys.exit(f"Invalid while run: {command}")
    elif '=' in command:  # Variable declaration/assignment
        var_name, var_value = command.split('=')
        var_name = var_name.strip()
        var_value = var_value.strip()

        # Check if the variable name is valid
        if not var_name.isidentifier():
            sys.exit(f"Invalid variable name: {var_name}")

        # Evaluate the variable value if it contains other variables
        for var in variables:
            if var in var_value:
                var_value = var_value.replace(var, str(variables[var]))
        try:
            var_value = eval(var_value)
        except:
            sys.exit(f"Invalid variable value: {var_value}")

        variables[var_name] = var_value
    elif command.startswith('printF[') and command.endswith(']'):  # Print variable value in specified format
        var_name = command[7:-1]
        if var_name in variables:
            print(variables[var_name])
        else:
            sys.exit(f"Variable not found: {var_name}")
    else:
        sys.exit(f"Invalid command {command}")

if len(sys.argv) < 2:
    print("Please provide the external file name as an argument.")
    sys.exit(1)

external_file = sys.argv[1]

if os.path.isfile(external_file) and external_file.endswith('.lenti'):
    with open(external_file, "r") as f:
        for line in f:
            print_in_program(line.strip())
else:
    print(f"Invalid filename: {external_file}")
