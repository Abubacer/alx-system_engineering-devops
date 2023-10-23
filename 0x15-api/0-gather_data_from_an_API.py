#!/usr/bin/python3
"""
Gathers data from 'jsonplaceholder' API. Returns for a given employee ID
information about his/her TODO list progress.
"""

from requests import get
import sys


def fetch_employee_todo_data(employee_id):
    """ Fetch TODO list progress data for a given employee id.

    Args:
        employee_id (int): The employee ID to get his/her TODO list progress.
    """
    api_url = "https://jsonplaceholder.typicode.com/users/"

    response = get("{}/{}".format(api_url, employee_id))

    data = response.json()
    employee_name = response.json().get("name")

    if employee_name is not None:
        todos_response = get("{}{}/todos".format(api_url, employee_id))
        todos_data = todos_response.json()

        total_number_tasks = len(todos_data)

        completed_tasks = []
        for task in todos_data:
            if task.get("completed") is True:
                completed_tasks.append(task)

        number_completed_tasks = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, number_completed_tasks, total_number_tasks
            )
        )

        for task in completed_tasks:
            title = task.get("title")
            print("\t {}".format(title))


if __name__ == "__main__":

    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])

    fetch_employee_todo_data(employee_id)
