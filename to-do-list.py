TASKS_FILE="tasks.txt"
tasks = {}
task_id = 1
def main():
    load_all_tasks()
    while True:
        show_activeTask()
        show_menu()
        choice = int(input("Enter your choice 1-5: "))
        if choice == 1:
            add_task()
        elif choice ==2:
            delete_task()
        elif choice == 3:
            display_tasks()
        elif choice == 4:
            mark_complete()
        elif choice == 5:
            print("good bye!")
            break
        else:
            print("Enter a valid Input")

def load_all_tasks():
    global tasks 
    global task_id
    tasks.clear()
    try:
        for line in open(TASKS_FILE, "r"):
            line = line.strip()
            tid, title, status = line.split("||")
            tasks[int(tid)] = {"title": title, "status": status}
            task_id = max(task_id, int(tid) + 1)
    except FileNotFoundError:
        print("No previous tasks found. Starting fresh!!!")

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add new task")
    print("2. Delete a task")
    print("3. Display my tasks")
    print("4. Mark as complete")
    print("5. Exit")

def add_task():
    global task_id
    title = input("Enter the task title: ").strip()
    if title == "":
        print("Task title cannot be empty.")
        return
    if title in [task["title"] for task in tasks.values()]:
        print("Task with this title already exists.")
        return
    tasks[task_id] = {"title": title, "status": "Not Completed"}
    print("Task " + title + " is successfully added with ID " + str(task_id))
    task_id += 1
    save_task()

def save_task():
    with open(TASKS_FILE, "w") as file:
        for tid, task in tasks.items():
            file.write(str(tid) + "||" + task["title"] + "||" + task["status"] + "\n")

def delete_task():
    try:
        tid= int(input("Enter the task ID to delete: "))
        if tid in tasks:
            print("Are you sure you want to delete task with ID " + str(tid) + "? (yes/no)")
            yORn = input()
            if yORn.lower() != 'yes' and yORn.lower() != 'y':
                print("Task deletion cancelled.")
                return
            else:
                del tasks[tid]
                print("Task with ID " + str(tid) + " has been deleted.")
        else:
            print("Task with ID " + str(tid) + " does not exist.")
    except ValueError:
        print("Please enter a valid task ID.")
    save_task()

def display_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- Task List ---")
        for tid, task in tasks.items():
            print("ID:"+ str(tid) + ", Title: " + task['title'] + ", Status: " + task['status'])

def mark_complete():
    try:
        tid = int(input("Enter the completed task's ID: "))
        if tid in tasks:
            tasks[tid]["status"] = "Completed"
            print("Task with ID " + str(tid) + " has been marked as completed.")
            save_task()
        else:
            print("Task with ID " + str(tid) + " does not exist.")
    except ValueError:
        print("Please enter a valid task ID.")

def show_activeTask():
    active_tasks = [tid for tid, task in tasks.items() if task["status"] == "Not Completed"]
    if active_tasks:
        print("\n--- Active Tasks ---")
        for tid in active_tasks:
            print("ID: " + str(tid) + ", Title: " + tasks[tid]["title"])
    else:
        print("No active tasks, create a new task.")
