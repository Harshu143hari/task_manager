# Python CLI Task Manager Application

## Project Description
This is a simple **Command-Line Interface (CLI)** application built in Python that allows users to manage tasks. The user can log in, add tasks, view tasks, delete tasks, mark tasks as complete, and save the tasks to a file. The application also ensures users have to log in before accessing the task manager, and they will be prompted to log in again after each session.

## Features
- **User Authentication**: The user must log in with predefined credentials (`test@example.com` and `password123`) to access the task manager.
- **Task Management**: The user can:
  - Add new tasks.
  - View all tasks (both completed and incomplete).
  - Delete tasks by ID.
  - Mark tasks as completed.
- **Task Persistence**: Tasks are saved to a file (`tasks.json`), and when the application is restarted, the tasks are loaded back into memory.
- **Re-login on Exit**: After choosing to "Save & Exit," the application will prompt the user to log in again.
  
## How to Run the Application

### 1. Prerequisites
- **Python 3.x** must be installed on your machine.
- Ensure you have the required libraries (none besides Python's standard libraries).

### 2. Running the Program
1. **Clone the repository or download the source code** to your local machine.
2. Open a terminal (or command prompt) in the directory where `task_manager.py` is located.
3. Run the program with the following command:
   ```bash
   python task_manager.py
