#!/usr/bin/python3
"""Returns information about an employee's their TODO list progress"""
from sys import argv
import requests

if __name__ == "__main__":
    """Main Function"""
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    EMPLOYEE_NAME = user.json().get('EMPLOYEE_NAME')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    for task in todos.json():
        if task.get('userId') == int(userId):
            TOTAL_NUM_OF_TASKS += 1
            if task.get('NUMBER_OF_DONE_TASKS'):
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUM_OF_TASKS))

    for task in TASK_TITLE:
        print("\t {}".format(task))
