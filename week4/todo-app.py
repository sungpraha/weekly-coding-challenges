# week4/todo_app.py

tasks = []  # This list will store our tasks (as dictionaries)

def add_task():
    """Prompts the user for a task description and adds it to the tasks list."""
    description = input("Enter task description: ")
    tasks.append({"description": description, "status": "pending"})
    print(f"Task '{description}' added.")

def view_tasks():
    """Displays all tasks with their status and a number."""
    if not tasks:
        print("No tasks in your to-do list!")
        return

    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks):
        # Display 1-based index to the user
        print(f"{index + 1}. [{task['status'].upper()}] {task['description']}")
    print("------------------")

def mark_task_complete():
    """Marks a specific task as complete."""
    view_tasks()
    if not tasks:
        return

    try:
        task_number_str = input("Enter the number of the task to mark as complete: ")
        task_number = int(task_number_str)

        # Adjust for 0-based indexing
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "complete"
            print(f"Task {task_number} ('{tasks[task_number - 1]['description']}') marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")


def remove_task():
    """Removes a specific task from the list."""
    view_tasks()
    if not tasks:
        return

    try:
        task_number_str = input("Enter the number of the task to remove: ")
        task_number = int(task_number_str)

        # Adjust for 0-based indexing
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['description']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Choose an action (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main application
if __name__ == "__main__":
    main_menu()