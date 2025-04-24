import json

file_name = 'list_todo.json'

def load_task():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except:
        return {'Tasks': []}

def save_task(tasks):
    try:
        with open(file_name, 'w') as file:
            json.dump(tasks,file)
    except:
        print("Failed to save tasks.")

def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List: ")
        for idx, task in enumerate(task_list,start=1):
            status = "[Completed]" if task.get("complete") else "[Pending]"
            print(f"{idx}. {task['description']} | {status}")


def add_task(tasks):
    description = input('Enter the task description: ').strip()
    if not description:
        print("Task description cannot be empty.")
        return
    else:
        tasks['tasks'].append({'description':description, 'complete': False})
        save_task(tasks)
        print(f'Task "{description}" added to the list.')
    
def mark_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input('Enter the task number to mark as completed: '))
        if 1 <= task_id <= len(tasks['tasks']):
            tasks['tasks'][task_id - 1]['complete'] = True
            save_task(tasks)
            print(f'Task {task_id} marked as completed.')
        else:
            print("Invalid task number.")
    except:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input('Enter the task number to delete: '))
        if 1 <= task_id <= len(tasks['tasks']):
            deleted_task = tasks['tasks'].pop(task_id - 1)
            save_task(tasks)
            print(f'Task "{deleted_task["description"]}" deleted from the list.')
        else:
            print('Invalid task number.')
    except ValueError:
        print('Invalid input. Please enter a number.')

def main():
    tasks = load_task()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

main()