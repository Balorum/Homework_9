CONTACTS = {
    "Nikita": "+380728364567",
    "Ivan": "+380926475937",
    "Mila": "+380916344924",
    "Filip": "+380927453420",
    "Henry": "+3808752088836",
    "Kirill": "+3804005448290",
    "Vika": "+380029466762",
}


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError as val:
            print(f"{args[0][-1]} is not a correct number")
        except KeyError as key:
            print(f"{args[0][1]} is not your contact")
        except IndexError as ind:
            print("You entered an invalid command")

    return wrapper


@input_error
def hello_handler(*args):
    if len(args[0]) != 1:
        raise IndexError
    print("How can I help you?")


@input_error
def add_handler(*args):
    if len(args[0]) != 3:
        raise IndexError
    int(args[0][2])
    CONTACTS[args[0][1]] = args[0][2]


@input_error
def change_handler(*args):
    if args[0][1] not in CONTACTS.keys():
        raise KeyError
    elif len(args[0]) != 3:
        raise IndexError
    else:
        CONTACTS[args[0][1]] = args[0][2]


@input_error
def phone_handler(*args):
    if len(args[0]) != 2:
        raise IndexError
    if args[0][1] not in CONTACTS.keys():
        raise KeyError
    else:
        print(CONTACTS[args[0][1]])


@input_error
def show_handler(*args):
    if len(args[0]) != 2:
        raise IndexError
    print("Your contacts")
    for key, val in CONTACTS.items():
        print(f"{key}: {val}")


@input_error
def exit_handler(*args):
    if len(args[0]) > 2:
        raise IndexError
    print("Good bye!")
    return "Good bye!"


COMMANDS = {
    "hello": hello_handler,
    "change": change_handler,
    "add": add_handler,
    "phone": phone_handler,
    "show": show_handler,
    "close": exit_handler,
    "exit": exit_handler,
    "good": exit_handler,
}


def get_handler(handler):
    return COMMANDS[handler]


def main():
    print(
        """
Hello, I am assistant-bot. My commands: \n
hello
add ...
change ...
phone ...
show all
close/exit/good bye 
"""
    )
    while True:
        handler = input("Введіть команду: ")
        command_list = handler.lower().split(" ")
        event_handler_list = handler.split(" ")
        if handler == ".":
            break
        event_handler = get_handler(command_list[0])
        end_flag = event_handler(event_handler_list)
        if end_flag == "Good bye!":
            break


if __name__ == "__main__":
    main()
