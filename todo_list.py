import argparse

class Task:
    def __init__(self, name, status='Pending'):
        self.name = name
        self.status = status

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(Task(task_name))

    
    def list_tasks(self):
        for task in self.tasks:
            print(f"- {task.name} ({task.status})")

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.status = 'Completed'
                break
    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def clear_tasks(self):
        self.tasks = []

def main():
    todo_list = ToDoListManager()
    
    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Mark a task as completed")
        print("4. Clear all tasks")
        print("5. Remove a task")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            todo_list.add_task(task_name)
            print(f"Task '{task_name}' added to the to-do list.")
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            task_name = input("Enter the task name to mark as completed: ")
            todo_list.mark_task_completed(task_name)
            print(f"Task '{task_name}' marked as completed.")
        elif choice == "4":
            todo_list.clear_tasks()
            print("All tasks cleared.")
        elif choice == "5":
            task_name = input("Enter the task name to remove: ")
            todo_list.remove_task(task_name)
            print(f"Task '{task_name}' removed from the to-do list.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()