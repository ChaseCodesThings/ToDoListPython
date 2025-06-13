def addTask(tasks):
    taskToAdd = input(f"Enter a task to add: ")
    tasks.append(taskToAdd)
    print(f"Task '{taskToAdd}' added.")

def removeTask(tasks):
    try:
        taskToRemove = int(input("Enter a task number to remove: "))
    except ValueError:
        print(f"'{taskToRemove}' is not a valid integer. Please enter a number.")
    if 1 <= taskToRemove <= len(tasks):
        print(f"Task #{taskToRemove} '{tasks[taskToRemove - 1]}' removed.")
        tasks.pop(taskToRemove - 1)
    else:
        print("Invalid task number.")

def listTasks(tasks):
    print("Current tasks:")
    if len(tasks) == 0:
        print("No tasks.")
    else:
        for i in range(len(tasks)):
            print(f"{i + 1}. " + tasks[i])
        print("")

def deleteAllTasks(tasks):
    tasks.clear()
    print("All tasks deleted.")