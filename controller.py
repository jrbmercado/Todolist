from task import Task
from user import User
import sys

current_user_id = "0"
current_user_first_name = "fName"
current_user_last_name = "lName"

def new_task():
    print("Creating new task")


def del_task():
    print("Deleting a task")


def edit_task():
    print("Editing task")


def complete_task():
    print("Completing task")


def attempt_login(input_login_id):
    user_dictionary = {}

    with open("user_database.txt", "r") as opened_user_database:
        lines = opened_user_database.read().splitlines()
        for line in lines:
            myList = line.split(",")
            if (myList[0] not in user_dictionary):
                user_dictionary[myList[0]] = [myList[1], myList[2]]
    if (input_login_id in user_dictionary):
        global current_user_id
        current_user_id = input_login_id
        global current_user_first_name
        current_user_first_name = user_dictionary[input_login_id][0].capitalize()
        global current_user_last_name
        current_user_last_name = user_dictionary[input_login_id][1].capitalize()
        return True
    else:
        return False

def logout():
    print("Exiting user")


def load_tasks():
    print("Loading tasks")


def main():
    input_login_id = input("What is your userID? ")
    if (attempt_login(input_login_id)):
        print(
            f"Welcome back {current_user_first_name} {current_user_last_name}")
    else:
        print("Welcome New User!")

    print("1 = Create new task")
    selection = input("Select an option: ")
    match selection:
        case "1":
            new_task()
        case "2":
            del_task()
        case "3":
            edit_task()
        case "4":
            complete_task()


if (__name__ == "__main__"):
    main()
