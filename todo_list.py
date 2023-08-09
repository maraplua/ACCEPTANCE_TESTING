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

    def clear_tasks(self):
        self.tasks = []

if __name__ == "__main__":
    todo_list = ToDoListManager()
    # Add your command-line interface here (e.g., using argparse or input())
