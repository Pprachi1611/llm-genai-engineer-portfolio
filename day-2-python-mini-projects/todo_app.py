import os
FILE_NAME = "tasks.txt"
def add_task():
    task = input("Enter new task: ").strip()
    
    if task == "":
        print(" Task cannot be empty!")
        return

    with open(FILE_NAME, "a") as f:
        f.write(task + "\n")

    print(" Task added successfully!")


def view_tasks():
    if not os.path.exists(FILE_NAME):
        print(" No tasks found.")
        return

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    if len(tasks) == 0:
        print(" No tasks available.")
        return

    print("\n Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")


def delete_task():
    if not os.path.exists(FILE_NAME):
        print(" No tasks to delete.")
        return

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    view_tasks()

    try:
        task_num = int(input("\nEnter task number to delete: "))

        if task_num < 1 or task_num > len(tasks):
            print(" Invalid task number!")
            return

        removed_task = tasks.pop(task_num - 1)

        with open(FILE_NAME, "w") as f:
            f.writelines(tasks)

        print(f" Deleted: {removed_task.strip()}")

    except ValueError:
        print(" Please enter a valid number!")


def main():
    while True:
        print("\n====== TO-DO APP ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice, try again!")


if __name__ == "__main__":
    main()