import utils
import data

def add_soldier(soldier_id: int, name: str) -> None:
    """
    מוסיפה חייל חדש למערכת.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        name (str): שם החייל
    
    מחזירה:
        None - הפונקציה מוסיפה את החייל או זורקת exception
    
    זורקת:
        ValueError: אם id כבר קיים במערכת
        ValueError: אם name ריק או לא תקין
    
    למה הפונקציה קיימת:
    לוגיקה עסקית טהורה של הוספת חייל.
    מבצעת בדיקות תקינות ומוסיפה את החייל לנתונים.
    לא מטפלת בקלט/פלט - רק בלוגיקה.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    allowed_length = 5
    if len(str(soldier_id)) != allowed_length  :
         raise ValueError(f'the maximum length of an id is only {allowed_length} numbers')
    elif utils.find_soldier_by_id(soldier_id):
         raise ValueError(f'this soldier id {soldier_id} is already in the system')
    elif not utils.is_valid_name(name):
         raise ValueError('error you entered an empty name')
    data.soldiers.append({'id': soldier_id,'name': name,'duties': []})
    return None


    
    


def remove_soldier(soldier_id: int) -> None:
    """
    מסירה חייל מהמערכת לפי id.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
    
    מחזירה:
        None - הפונקציה מסירה את החייל או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הסרת חייל.
    מבצעת בדיקת קיום ומסירה מהנתונים.
    זורקת exception במקרה שהחייל לא קיים.
    """
    pass


def get_all_soldiers() -> list:
    """
    מחזירה את רשימת כל החיילים במערכת.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת: כלום
    
    מחזירה:
        list: רשימה של מילונים, כל מילון מייצג חייל
              רשימה ריקה אם אין חיילים
    
    זורקת: כלום - תמיד מחזירה רשימה (ריקה או מלאה)
    
    למה הפונקציה קיימת:
    גישה לנתונים בצורה מבוקרת.
    מאפשר לקבל את הנתונים מבלי לגשת ישירות למשתנה הגלובלי.
    """
    pass


if __name__ == '__main__':
    print(add_soldier(10042,' '))
    print(data.soldiers)