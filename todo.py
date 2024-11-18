class TodoListManager:
    ALLOWED_STATUSES = {'todo', 'inProgress', 'done'}

    def __init__(self):
        self.task_storage = {}
        self.task_counter = 1

    def add_task(self, description, status='todo'):
        if not isinstance(description, str) or not isinstance(status, str):
            raise TypeError("INVALIDE_ARGUMENT")
        if status not in self.ALLOWED_STATUSES:
            raise ValueError("INVALIDE_STATUS")

        self.task_storage[self.task_counter] = {
            'details': description,
            'state': status
        }
        self.task_counter += 1

    def remove_task(self, task_id):
        if not isinstance(task_id, int):
            raise TypeError("INVALIDE_ARGUMENT")
        return self.task_storage.pop(task_id, None) is not None

    def update_status(self, task_id, new_status):
        if not isinstance(task_id, int) or not isinstance(new_status, str):
            raise TypeError("INVALIDE_ARGUMENT")
        if new_status not in self.ALLOWED_STATUSES:
            raise ValueError("INVALIDE_STATUS")
        if task_id not in self.task_storage:
            return False
        if self.task_storage[task_id]['state'] == new_status:
            return False

        self.task_storage[task_id]['state'] = new_status
        return True

    def display_tasks(self):
        grouped_tasks = {'todo': [], 'inProgress': [], 'done': []}
        for task_id, task_info in self.task_storage.items():
            grouped_tasks[task_info['state']].append(
                f'  {task_id} "{task_info["details"]}"'
            )

        print("Todo:\n" + ("\n".join(grouped_tasks['todo']) or "-"))
        print("In Progress:\n" + ("\n".join(grouped_tasks['inProgress']) or "-"))
        print("Done:\n" + ("\n".join(grouped_tasks['done']) or "-"))

# Примеры использования
todo_manager = TodoListManager()

try:
    todo_manager.add_task('create a task')
    todo_manager.add_task('make a bed', 'todo')
except Exception as err:
    print(f"Error: {err}")

try:
    print(todo_manager.update_status(1, 'inProgress'))  # True
    print(todo_manager.update_status(1, 'done'))        # True
    print(todo_manager.update_status(1, 'done'))        # False
except Exception as err:
    print(f"Error: {err}")

try:
    print(todo_manager.remove_task(1))  # True
    print(todo_manager.remove_task(1))  # False
except Exception as err:
    print(f"Error: {err}")

todo_manager.display_tasks()
