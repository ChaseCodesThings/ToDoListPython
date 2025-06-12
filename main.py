def main():
    tasks = []
    def addTask():
        taskToAdd = input(f"Enter a task to add: ")
        tasks.append(taskToAdd)
    def removeTask():
        taskToRemove = int(input("Enter a task number to remove: "))
        print(f"Task #{taskToRemove} '{tasks[taskToRemove - 1]}' removed")
        tasks.pop(taskToRemove - 1)
    def listTasks():
        print("Current tasks:")
        for i in range (len(tasks)):
            print(f"{i + 1}. " + tasks[i])
        print("")
    def deleteAllTasks():
        for i in range(len(tasks)):
            tasks.pop(i)
    print("Welcome to your To-Do List!")
    #choice = input("1. Add a task\n2. Remove a task\n3. List all tasks\n4. Delete all tasks\n5. Exit\nEnter your choice: ")
    choice = 0
    while choice != "5":
        choice = input(
            "1. Add a task\n2. Remove a task\n3. List all tasks\n4. Delete all tasks\n5. Exit\nEnter your choice: ")
        if choice == "1":
            addTask()
        elif choice == "2":
            removeTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            deleteAllTasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    print("Thanks for using our To-Do List!\nHave a productive day!")
if __name__ == "__main__":
    main()