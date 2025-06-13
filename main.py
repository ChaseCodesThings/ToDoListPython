from functions import *
def main():
    tasks = []
    print("Welcome to your To-Do List!")
    choice = 0
    menu = """
    1. Add a task
    2. Remove a task
    3. List tasks
    4. Delete all tasks
    5. Exit
    """
    while choice != "5":
        choice = input(menu + "Enter your choice: ")
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