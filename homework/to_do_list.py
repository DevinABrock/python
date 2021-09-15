###############################################################################################################################################################################
### To-Do List
###############################################################################################################################################################################
import pickle

with open('todos.pickle', 'rb') as fh:
    todos = pickle.load(fh)

def delete_task(delete_priority , delete_position):
    del todos[delete_priority][delete_position]

def rename_task(rename_priority , rename_position, new_task):
    todos[rename_priority][rename_position] = new_task

def add_task(user_input):
    set_priority = input("Which is the priority: High, Medium, or Low?: ")
    set_task = input("Adding a task: ")
    if set_priority == "high":
        todos["high"].append(set_task)
    elif set_priority == "medium":
        todos["medium"].append(set_task)
    elif set_priority == "low":
        todos["low"].append(set_task)
    else:
        print("Invalid")
    print(todos)

def print_list():
    print(todos)

task_list = []
set_task = ()
while True:
    user_input = input("Press 1 to add task, Press 2 to delete task, Press 3 to update a task, Press 4 to view all tasks, Press q to quit: ")
    if user_input == "1":
        add_task(user_input)
    elif user_input == "2":
        delete_priority = input("Priority?")
        delete_position = int(input("task number?")) - 1
        delete_task(delete_priority , delete_position)
    elif user_input == "3":
        rename_priority = input("Priority?")
        rename_position = int(input("task number?")) - 1
        new_task = input("New Task")
        rename_task(rename_priority , rename_position, new_task)
    elif user_input == "4":
        print_list()
    elif user_input.lower() == "q":
        print ("Quitting todo list")
        with open('todos.pickle', 'wb') as fh :
            pickle.dump(todos, fh)
        break
    else:
        print("Not a valid input")







