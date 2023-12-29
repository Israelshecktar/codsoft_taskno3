def welcome():
  """This function displays a welcome message"""
  print("Welcome to Shecktar To-Do List App")

def add_task(name):
  """This function adds a new task to the list"""
  task = {"name": name, "completed": False}
  tasks.append(task)

def update_task(index):
  """This function updates the status of a task"""
  if len(tasks) > index:
      task = tasks[index]
      task["completed"] = not task["completed"]
      print("Task updated.")
  else:
      print("No task found at that index.")

def delete_task(index):
  """This function deletes a task from the list"""
  if len(tasks) > index:
      del tasks[index]
      print("Task deleted.")
  else:
      print("No task found at that index.")

def view_tasks():
  """This function displays all tasks"""
  if tasks:
      for i, task in enumerate(tasks):
          status = "done" if task["completed"] else "not done"
          print(f"{i}. {task['name']} - {status}")
  else:
      print("No tasks available.")

def main():
  welcome()

  tasks = []
  while True:
      print("\nSelect operation:")
      print("1. Add task")
      print("2. Update task")
      print("3. Delete task")
      print("4. View tasks")
      print("5. Exit")

      operation = input("Enter choice (1/2/3/4/5): ")

      if operation == '1':
          name = input("Enter task name: ")
          add_task(name)
          print("Task added.")

      elif operation == '2':
          view_tasks()
          index = int(input("Enter task number: "))
          update_task(index)

      elif operation == '3':
          view_tasks()
          index = int(input("Enter task number: "))
          delete_task(index)

      elif operation == '4':
          view_tasks()

      elif operation == '5':
          break

      else:
          print("Invalid input")

if __name__ == "__main__":
  main()
