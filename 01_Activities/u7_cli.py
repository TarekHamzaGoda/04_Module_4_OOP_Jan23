import os

def list_files():
    print("Contents of current directory:")
    for item in os.listdir():
        print(item)

def add_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("Result: ", result)

def help():
    print("Commands available:")
    print("LIST - List contents of current directory")
    print("ADD - Add two numbers")
    print("HELP - Show available commands")
    print("EXIT - Exit the shell")

# Main loop of the command shell
while True:
    command = input("Enter command (LIST, ADD, HELP, EXIT): ").upper()

    if command == "LIST":
        list_files()
    elif command == "ADD":
        add_numbers()
    elif command == "HELP":
        help()
    elif command == "EXIT":
        print("Exiting the shell...")
        break
    else:
        print("Invalid command. Please try again.")