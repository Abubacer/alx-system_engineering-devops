#!/usr/bin/python3
"""
Gathers data from 'jsonplaceholder' API. Returns for a given employee ID
information about his/her TODO list progress.

Export the gathed data in the CSV format.
"""

import csv
from requests import get
import sys


def export_user_data(user_id):
    """ Records all tasks that are owned by the user, and export
    the gathed data in CSV format.

    Args:
        user_id (int): The user ID to export his data.
    """
    api_url = "https://jsonplaceholder.typicode.com/"

    response = get("{}users/{}".format(api_url, user_id))

    user_name = response.json().get("username")

    if user_name is not None:
        todos_data = get("{}users/{}/todos".format(api_url, user_id)).json()

    with open("{}.csv".format(user_id), 'w', newline='') as csv_file:
        write_data = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            write_data.writerow([int(user_id),
                                user_name,
                                task.get("completed"),
                                task.get("title")])


if __name__ == "__main__":

    if len(sys.argv) > 1:
        user_id = int(sys.argv[1])

    export_user_data(user_id)
