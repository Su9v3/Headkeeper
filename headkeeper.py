import datetime
import json
import curses
import pathlib

# Functions
def createTasksFile():

    basicData = []
    with open("tasks.json", "w") as writeFile:
        json.dump(basicData, writeFile)

def displayTasks():
    pass

def addTask():

    name = input("Task Name: ")
    details = input('Task Details: ')
    dueYear = input('Due Year: ')
    dueMonth = input('Due Month: ')
    dueDate = input('Due Date: ')

    task = {"Name": name, 'Details': details, 'DueYear': dueYear, 'DueMonth': dueMonth, 'DueDate': dueDate}

    existingTasks = []

    with open('tasks.json', 'r') as readFile:
        existingTasks = json.load(readFile)
        existingTasks.append(task)

    with open('tasks.json', 'w') as writeFile:
        json.dump(existingTasks, writeFile)

def addToTask():
    pass

# Switches to GUI mode
def guiMode():
    pass

# Switches to TUI mode
def tuiMode():
    pass

def calculateTimeLeft(tasknum):
    with open(tasksFile, 'r') as readFile:
        tasks = json.load(readFile)

    task = tasks[int(tasknum)]

    if(task['DueYear'].isdecimal() and task['DueMonth'].isdecimal() and task['DueDate'].isdecimal()):
        dueYear = int(task['DueYear'])
        dueMonth = int(task['DueMonth'])
        dueDate = int(task['DueDate'])
        dueTime = datetime.datetime(dueYear, dueMonth, dueDate)

        timeLeft = dueTime - datetime.datetime.now()

        print(timeLeft)

        return(dueTime.date())

    else:
        return("Unrecongnized Time")

# Universal variables
tasksFile = pathlib.Path("tasks.json")

# Program starts here
# Checks if tasks.json already exists, if not creates file.
if(tasksFile.exists() == False):
    createTasksFile()

with open(tasksFile, 'r') as readFile:
    data = json.load(readFile)

    print(data)

i = 0

'''
while i != len(data):
    task = data[i]
    print('Task: {num}'.format(num = i))
    print('Name: {name}'.format(name = task['name']))
    print('Due Date: {duedate}'.format(duedate =  task['due']))
    print('\n')
    i += 1
'''
print(datetime.datetime.now())
calculateTimeLeft(0)