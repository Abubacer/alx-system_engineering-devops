#!/usr/bin/python3
"""
Gathers data from 'jsonplaceholder' API. And returns for a given employee ID
information about his/her TODO list progress.

Records all tasks from all employees.

Export the gathed data in the JSON format. Format:
{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}

File name: todo_all_employees.json
"""

import json
from requests import get


def export_all_employees_data():
    """ Records all tasks from all employees, and export
    the gathed data in JSON format.
    """
    api_url = "https://jsonplaceholder.typicode.com/"

    users = get("{}users".format(api_url)).json()

    user_data = {}

    for user in users:
        user_id = user.get("id")
        user_name = user.get("username")
        todos_data = get("{}users/{}/todos".format(api_url, user_id)).json()
        tasks_records = []
        for task in todos_data:
            task_dict = {
                "username": user_name,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            tasks_records.append(task_dict)

        user_data[user_id] = tasks_records

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(user_data, json_file)


if __name__ == "__main__":

    export_all_employees_data()
