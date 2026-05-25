import os

def load_pass(file_name):
    msn_lst=[]
    """:dicts של רשימה ומחזירה הקובץ את קוראת
   [{'id': 1, 'status': 'PENDING', 'desc': 'ללמוד Python'}, ...]  """
    if not os.path.exists(file_name):
        return msn_lst
    with open(file_name,"r", encoding="utf-8") as f:
        for line in f.readlines():
            if not line.strip():
                continue
            new_line=line.split("|")
            msn_lst.append({"id":new_line[0].strip(),"status":new_line[1].strip(),"desc":new_line[2].strip()})
        return msn_lst
print(load_pass("tasks.txt"))

def save_tasks(file_name,tasks):
    """
    שומרת את רשימת המשימות לקובץ בפורמט id|status|description
    """
    with open(file_name,"w",encoding="utf-8") as f:
        for task in tasks:
            f.write(f"{task['id']}|{task['status']}|{task['desc']}\n")

def add_task(file_name,description):
    """ חדשה משימה מוסיפה
    - ID = הבאה המשימה מספר
    - status = 'PENDING'
    - description = שניתן הפרמטר """
    all_tasks=load_pass(file_name)
    all_tasks.append({"id":len(all_tasks),"status":"Pending","desc":description})
    save_tasks(file_name,all_tasks)

def complete_task(file_name,task_id):
    """DONE-ל PENDING-מ task_id משימה של status את משנה
  שגיאה הודעת מדפיסה — קיים לא ID-ה"""
    all_tasks=load_pass(file_name)
    is_exists=False
    for dct in all_tasks:
        if task_id==int(dct["id"]):
            dct["status"]="DONE"
            is_exists=True
    if not is_exists:
        print("Error: the id was not found")
    save_tasks(file_name, all_tasks)
complete_task("tasks.txt",1)

def list_tasks(file_name):
    """
     מציגה את כל המשימות בפורמט מסודר
    """
    tasks=load_pass(file_name)
    for task in tasks:
        if task["status"]=="DONE":
            print(f"{task['id']}|[V]|{task['desc']}")
        else:
            print(f"{task['id']}|[X]|{task['desc']}")

list_tasks("tasks.txt")

# def main():
#     FILENAME = "tasks.txt"
#     while True:
#         print('\n=== To-Do List Manager ===')
#         print('הצג משימות 1.')
#         print('הוסף משימה 2.')
#         print('סמן כהושלם 3.')
#         print('יציאה 4.')
#         choice = input('בחירה:')
#         if choice == '1':
#             list_tasks(FILENAME)
#         elif choice == '2':
#             desc = input(' :תיאור המשימה')
#             add_task(FILENAME, desc)
#             print ('!המשימה נוספה')
#         elif choice == '3':
#             task_id = int(input('משימה מספר:'))
#             complete_task(FILENAME, task_id)
#         elif choice == '4':
#             print('!להתראות')
#             break
#         else:
#             print('בחירה לא תקינה')
# if __name__ == '__main__':
#     main()
