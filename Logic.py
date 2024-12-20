from PyQt6.QtCore import Qt

class APPLogic:
    def __init__(self):
        #Structure: {'id': int, 'name': str, 'category': str, 'priority': str, 'completed': bool}
        self.tasks = []
        self.task_id_counter = 0

    def add_task(self, task_input):
        """
        Add a new task to the task list.
        :param task_input: Task details as a string in the format "name, category, priority".
        :return: Success message or error message.
        """
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
            return "Error: Task input MUST be in the format 'name, category, priority'."

    def mark_completed(self, task_id):
        """
        Mark a task as completed.
        :param task_id: ID of the task to mark as completed.
        :return: Success message or error message.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return "Task marked as completed!"
        return "Error: Task ID not found."

    def delete_task(self, task_id):
        """
        Delete a task by ID.
        :param task_id: ID of the task to delete.
        :return: Success message or error message.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return "Task deleted successfully!"
        return "Error: Task ID not found."

    def search_tasks(self, keyword):
        """
        Search tasks by a keyword.
        :param keyword: Keyword to search for in task names, categories, or priorities.
        :return: List of matching tasks.
        """
        keyword = keyword.lower()

        matching_tasks = [] # Initialize an empty list to store matching tasks

        for task in self.tasks:
            task_name = task["name"].lower()
            task_category = task["category"].lower()
            task_priority = task["priority"].lower()

            # Check if the keyword is present in any of the fields
            if (keyword in task_name or
                keyword in task_category or
                keyword in task_priority):
                matching_tasks.append(task) # Add the matching task to the result list

        return matching_tasks


    def get_all_tasks(self):
        """
        Get all tasks.
        :return: List of all tasks.
        """
        return self.tasks

    def get_completed_tasks(self):
        """
        Get all completed tasks.
        :return: List of completed tasks.
        """
        return [task for task in self.tasks if task["completed"]]

    def get_uncompleted_tasks(self):
        """
        Get all uncompleted tasks.
        :return: List of uncompleted tasks.
        """
        return [task for task in self.tasks if not task["completed"]]
