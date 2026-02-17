from core.assistant  import process_command

def main():
    print("Jarvis CLI started. Type 'exit to quit.")

    while True:
        command = input("You: ")

        if command.lower() == "exit":
            break
    
        process_command(command)

if __name__ == "__main__":
    main()