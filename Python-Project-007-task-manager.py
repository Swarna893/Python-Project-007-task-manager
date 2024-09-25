# Python-Project-007-task-manager


# To-Do List Application

# List to store tasks
tasks = []

# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("\nNo tasks in the to-do list.")
    else:
        print("\nTasks in the to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to add a task
def add_task():
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")

# Function to remove a task
def remove_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' has been removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main function to run the application
def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                remove_task()
            elif choice == 4:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")

# Run the application
if __name__ == "__main__":
    main()
