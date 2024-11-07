class InvalidArgumentError(Exception):
    pass

class InvalidStatusError(Exception):
    pass

class Task:
    def __init__(self, description, status='todo'):
        self.description = description
        self.status = status

class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description, status='todo'):
        if not isinstance(description, str):
            raise InvalidArgumentError('INVALID_ARGUMENT')
        if status not in ['todo', 'inProgress', 'done']:
            raise InvalidStatusError('INVALID_STATUS')

        task = Task(description, status)
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)

    def delete_task(self, id):
        if not isinstance(id, int):
            raise InvalidArgumentError('INVALID_ARGUMENT')

        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                return True
        return False

    def change_status(self, id, status):
        if not isinstance(id, int):
            raise InvalidArgumentError('INVALID_ARGUMENT')
        if status not in ['todo', 'inProgress', 'done']:
            raise InvalidStatusError('INVALID_STATUS')

        for task in self.tasks:
            if task.id == id:
                if task.status == status:
                    return False
                task.status = status
                return True
        return False

    def show_list(self):
        todo_tasks = [task for task in self.tasks if task.status == 'todo']
        in_progress_tasks = [task for task in self.tasks if task.status == 'inProgress']
        done_tasks = [task for task in self.tasks if task.status == 'done']

        print("Todo:")
        for task in todo_tasks:
            print(f"  {task.id} \"{task.description}\"")

        print("In Progress:")
        for task in in_progress_tasks:
            print(f"  {task.id} \"{task.description}\"")

        print("Done:")
        for task in done_tasks:
            print(f"  {task.id} \"{task.description}\"")

# Пример использования:
todo_list = TodoList()

try:
    todo_list.add_task('create a task')
    todo_list.add_task('make a bed')
    todo_list.add_task('write a post', 'inProgress')
    todo_list.add_task('descr', '')  # error INVALID_STATUS
except (InvalidArgumentError, InvalidStatusError) as e:
    print(e)

try:
    todo_list.add_task(123, 'todo')  # error INVALID_ARGUMENT
except (InvalidArgumentError, InvalidStatusError) as e:
    print(e)

try:
    todo_list.add_task(['descr'], 'todo')  # error INVALID_ARGUMENT
except (InvalidArgumentError, InvalidStatusError) as e:
    print(e)

print("Initial list:")
todo_list.show_list()

print("\nChanging statuses:")
try:
    print(todo_list.change_status(1, 'inProgress'))  # true
    print(todo_list.change_status(2, 'done'))  # true
    print(todo_list.change_status(2, 'done'))  # false (already has the value)
    print(todo_list.change_status(1, 'notTodo'))  # error INVALID_STATUS
except (InvalidArgumentError, InvalidStatusError) as e:
    print(e)

print("\nDeleting tasks:")
try:
    print(todo_list.delete_task(1))  # true
    print(todo_list.delete_task(1))  # false (already deleted)
except (InvalidArgumentError, InvalidStatusError) as e:
    print(e)

print("\nFinal list:")
todo_list.show_list()
