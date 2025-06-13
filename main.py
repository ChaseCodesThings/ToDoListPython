from functions import *
def main():
    tasks = []
    print("Welcome to your To-Do List!")
    choice = 0
    while choice != "5":
        choice = input("1. Add a task\n2. Remove a task\n3. List all tasks\n4. Delete all tasks\n5. Exit\nEnter your choice: ")
        if choice == "1":
            addTask(tasks)
        elif choice == "2":
            removeTask(tasks)
        elif choice == "3":
            listTasks(tasks)
        elif choice == "4":
            deleteAllTasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    print("Thanks for using our To-Do List!\nHave a productive day!")
if __name__ == "__main__":
    main()