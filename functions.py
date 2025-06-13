def addTask(tasks):
    taskToAdd = input(f"Enter a task to add: ")
    tasks.append(taskToAdd)

def removeTask(tasks):
    taskToRemove = int(input("Enter a task number to remove: "))
    if taskToRemove > 0 & taskToRemove <= len(tasks):
        print(f"Task #{taskToRemove} '{tasks[taskToRemove - 1]}' removed")
        tasks.pop(taskToRemove - 1)
    else:
        print("Invalid task number.")

def listTasks(tasks):
    print("Current tasks:")
    for i in range(len(tasks)):
        print(f"{i + 1}. " + tasks[i])
    print("")

def deleteAllTasks(tasks):
    for i in range(len(tasks)):
        tasks.pop(i)