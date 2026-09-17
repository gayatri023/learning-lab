"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""
tasks = []

def add_task():
	task = input("Add the task: ")
	tasks.append(task)

def view_tasl():
	print("\nYour Tasks:")

	for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def completed_task():
	

while True:
	print("Add a task")
	print("2. View Tasks")
    	print("3. Mark Task as Completed")
    	print("4. Delete Task")
    	print("5. Exit")

	choice = input("Choose an option: ")

	if choice == "1":
		add_task()
	elif choice == "2":
		view_tasks()
	elif choice == "3":
		completed_task()
	elif choice == "4":
		delete_task()
	elif choice == "5"
		break
