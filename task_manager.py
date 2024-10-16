import json  # For file handling

# Task class
class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __repr__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"ID: {self.id}, Title: '{self.title}', Status: {status}"

# Global list to store tasks
tasks = []

# Task management functions
def add_task(title):
    id = len(tasks) + 1
    new_task = Task(id, title)
    tasks.append(new_task)
    print(f"Task '{title}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(task)

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    print(f"Task with ID {task_id} deleted successfully.")

def complete_task(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Task with ID {task_id} marked as completed.")
            break
    else:
        print(f"No task found with ID {task_id}.")

# File handling functions
def save_tasks(filename="tasks.json"):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)
    print("Tasks saved to tasks.json.")

def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            tasks = [Task(**data) for data in tasks_data]
        print("Tasks loaded from tasks.json.")
    except FileNotFoundError:
        print("No saved tasks found. Starting with an empty task list.")
        tasks = []

# Login function with a loop to re-prompt on invalid credentials
def login():
    while True:
        email = input("Enter email: ")
        password = input("Enter password: ")
        # Check against dummy credentials
        if email == "test@example.com" and password == "password123":
            print("Login successful!")
            return True
        else:
            print("Invalid credentials. Please try again.")

# Task manager function after successful login
def task_manager():
    load_tasks()  # Load tasks when the program starts
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a numerical task ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                complete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a numerical task ID.")
        elif choice == '5':
            save_tasks()
            print("Goodbye! You will be asked to log in again.")
            break
        else:
            print("Invalid choice. Please try again.")

# Main loop to ensure re-login after exit
def main():
    while True:  # Infinite loop to allow re-login
        print("\nWelcome! Please log in to access the Task Manager.")
        login()  # Prompt login
        task_manager()  # Start the task manager after successful login
        print("Session ended. You will now be prompted to log in again.\n")

# Entry point
if __name__ == "__main__":
    main()
