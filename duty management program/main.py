import data

def print_menu():
    """print menu to user
    parameter : none
    return : none """
    
    print("""MENU
press 1 show soldiers
press 2 add a solider
press 3 remove a soldier
press 4 add a duty to a soldier
press 5 update a duty to a soldier
press 6 show a soldier duty""")

def get_user_choice():
    user_input = input('enter a number between 1 - 6 : ')
    return user_input



def main():
    run_program = True
    while run_program:
        print_menu()

