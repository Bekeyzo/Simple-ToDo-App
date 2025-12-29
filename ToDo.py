task_list = []
def add_task():
    enter_task = input("Enter task: ")
    task_list.append(enter_task)

def remove_task():
    remove_task = input("Enter task to remove: ")
    if remove_task in task_list:
        task_list.remove(remove_task)
    else:
        print("Task not found")

def view_task():
    print(task_list)

while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Task")
    print("4. Exit")
    choice = int(input("Choose (1-4): "))
    if choice == 1:
        add_task()
    elif choice == 2:
        remove_task()
    elif choice == 3:
        view_task()
    elif choice == 4:
        break
    else:
        print("Invalid Choice, Try Again") 
