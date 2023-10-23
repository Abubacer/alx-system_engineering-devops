#!/usr/bin/python3
"""
Gathers data from 'jsonplaceholder' API. Returns for a given employee ID
information about his/her TODO list progress.

Export the gathed data in the JSON format. Format:
{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

File name: USER_ID.json
"""

import json
from requests import get
import sys


def export_user_data(user_id):
    """ Records all tasks that are owned by the user, and export
    the gathed data in JSON format.

    Args:
        user_id (int): The user ID to export his data.
    """
    api_url = "https://jsonplaceholder.typicode.com/"

    response = get("{}users/{}".format(api_url, user_id))
    user_name = response.json().get("username")

    todos_data = get("{}users/{}/todos".format(api_url, user_id)).json()

    tasks_records = []
    for task in todos_data:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = user_name
        tasks_records.append(task_dict)

    data = {user_id: tasks_records}

    with open("{}.json".format(user_id), 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        user_id = int(sys.argv[1])

    export_user_data(user_id)
