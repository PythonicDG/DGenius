from core.parser import parse_command

def process_command(command):
    action = parse_command(command)
    print("Parsed Action:", action)