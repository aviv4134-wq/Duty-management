import data,solider_manager,duty_manager

def print_menu() -> None:
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



def get_user_choice() -> str:
        """
        מקבלת בחירה מהמשתמש.
        
        מקבלת: כלום
        מחזירה: מחרוזת המייצגת את בחירת המשתמש
        
        למה הפונקציה קיימת:
        הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
        מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
        """
        user_input = input('enter a number between 1 - 6 : ')
        check_user_choisce(user_input)
        return user_input

def check_user_choisce(user_input):
    if not user_input.isdigit():
        raise ValueError("only 1 - 6 numbers allowed")
    elif not 1 <= int(user_input) <= 6 :
       raise ValueError("only 1 - 6 numbers allowed")
    
    return None
    
    

def handle_add_soldier() -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """
    
    soldier_id = input('enter soldier id: ')
    check_user_id_input(soldier_id)
    soldier_id = int(soldier_id)
    soldier_name = input('enter soldier name: ')
    solider_manager.add_soldier(soldier_id,soldier_name)
    return None



def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = input('enter soldier id: ')
    check_user_id_input(soldier_id)
    soldier_id = int(soldier_id)
    solider_manager.remove_soldier(soldier_id)
    return None


def check_user_id_input(soldier_id):
    """check if the user input is only numbers
    
    taken : user input id soldier
    return: None"""
    
    if not soldier_id.isdigit():
        raise ValueError('enter only numbers')
    return None


def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    pass


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = input('enter soldier id: ')
    check_user_id_input(soldier_id)
    soldier_id = int(soldier_id)
    duty_name_input = input('enter soldier duty name: ')
    day_input = input('enter day except weekends: ')
    duty_manager.add_duty_to_soldier(soldier_id,duty_name_input,day_input)
    return None


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass



def main():
    run_program = True
    while run_program:
        print_menu()
        try:   
            user_choise = get_user_choice()
            if user_choise == 1:
                pass
            elif user_choise == 2:
                handle_add_soldier()
            elif user_choise == 3:
                handle_remove_soldier()
            elif user_choise == 4:
                pass
            elif user_choise == 5:
                pass
            elif user_choise == 6:
                pass
        except Exception as error:
               print(error)
               continue

#main()
print(data.soldiers)