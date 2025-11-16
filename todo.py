Task_to_do=[]
def todolist():
    n=input("DO you want to add a new task in your to-do list \n Yes/No")
    if n.lower()=="yes":
        d=input("Name of the task")
        Task_to_do.append(d)
        todolist()
    elif n.lower()=="no":
        print("Your to-do list is as follows \n",Task_to_do)
    else:
        print("Choice is not as required")
def to_remove():
    n=input("DO you want to remove a task in your to-do list \n Yes/No")
    if n.lower()=="yes":
        d=input("Enter name of task you want to remove")
        if d in Task_to_do:
            print(Task_to_do.pop(d),"is removed succesfully")
        else:
            print("There is no such task named:",d)
    elif n.lower()=="no":
        print("Your updated to-do list is ",Task_to_do)
    else:
        print("Choice is not as required")
def file():
    f=open("To_do_list.txt","a")
    print(Task_to_do,file=f)
todolist()
to_remove()
file()