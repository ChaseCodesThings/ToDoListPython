def main():
    tasks = []
    def addTask():
        task = input("Enter a task: ")
        tasks.append(task)
        print(f"Task '{task}' added to the list.")
    def listTasks(tasks):
        if not tasks:
            print("No tasks added.")
        else:
            print("Current tasks:")
            for index, tasks in enumerate(tasks):
                print(f"Task #{index + 1}. {tasks}")
    def removeTask():
        listTasks(tasks)
        try:
            taskToRemove = int(input("Enter the task number to remove: "))
            tasks.pop(taskToRemove - 1)
            print(f"Task '#{taskToRemove}' removed from the list.")
        except:
            print("Invalid input.")
    while True:
        print("\n")
        print("Select one of the following options:")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            addTask()
        elif choice == "2":
            removeTask()
        elif choice == "3":
            listTasks(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid input")
    print("\nGoodbye!")
if __name__ == "__main__":
    main()