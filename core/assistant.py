from core.parser import parse_command

def process_command(command):
    action = parse_command(command)
    print("Parsed Action:", action)

def process_input(user_input):
    print("Processing input:", user_input)
    process_command(user_input)