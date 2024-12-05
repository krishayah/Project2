from PyQt6.QtCore import Qt

class APPLogic:
    def __init__(self):
        #Structure: {'id': int, 'name': str, 'category': str, 'priority': str, 'completed': bool}
        self.tasks = []
        self.task_id_counter = 0

    def add_task(self, task_input):

        try:
            name, category, priority = map(str.strip, task_input.split(","))
            self.task_id_counter += 1
            task = {
                "id": self.task_id_counter,
                "name": name,
                "category": category,
                "priority": priority,
                "completed": False,
            }
            self.tasks.append(task)
            return "Task added successfully!"
        except ValueError:
            return "Error: Task input should be in the format 'name, category, priority'."

    def mark_completed(self, task_id):

        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return "Task marked as completed!"
        return "Error: Task ID not found."


    def delete_task(self, task_id):

        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return "Task deleted successfully!"
        return "Error: Task ID not found."

    def search_tasks(self, keyword):

        return [
            task
            for task in self.tasks
            if keyword.lower() in task["name"].lower()
               or keyword.lower() in task["category"].lower()
               or keyword.lower() in task["priority"].lower()
        ]

    def get_all_tasks(self):

        return self.tasks
