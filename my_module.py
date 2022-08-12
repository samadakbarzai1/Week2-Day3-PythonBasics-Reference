
# hope to recive 5

usr_input_global = []

def user_choice():
    user_ch =  int(input("1: Add items in the list\n2: Delete item in the list\n3: see your current shopping list\n4: quit\n"))
    if user_ch == 1:
        add_items()
    elif user_ch == 2:
        del_items()
    elif user_ch == 3:
        current_items()
    elif user_ch == 4:
        program_quit()
    else:
        print("Wrong selection please choose a correct option")


def add_items():
    user_input = str(input("enter your list items seperated by comma(,):  "))
    list_of_user_input = user_input.split(",")
    for x in list_of_user_input:
        usr_input_global.append(x)
    print(usr_input_global,end="\n")
    user_choice()


def del_items():
    del_option = str(input("for clearing the list write clear: "))
    if del_option == 'clear':
        usr_input_global.clear()
    user_choice()


def current_items():
    for x in usr_input_global:
        print(x)
    user_choice()

def program_quit():
    for x in usr_input_global:
        print(x)
    quit()


user_choice()
    