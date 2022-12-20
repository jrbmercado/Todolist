from task import Task
from user import User
import sys

global current_user_id
global current_user_first_name
global current_user_last_name


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

    print(f"Looking for {input_login_id}")

    with open("user_database.txt", "r") as opened_user_database:
        lines = opened_user_database.read().splitlines()
        for line in lines:
            myList = line.split(",")
            if (myList[0] not in user_dictionary):
                print("UserID is not in dictionary, adding to dictionary")
                user_dictionary[myList[0]] = [myList[1], myList[2]]
            else:
                print("Skipping add to dictionary, userID already exists")
    print(user_dictionary)
    if (input_login_id in user_dictionary):
        print("Found")
        current_user_id = input_login_id
        current_user_first_name = user_dictionary[input_login_id][0]
        current_user_last_name = user_dictionary[input_login_id][1]
        return True
    else:
        print("Not found")
        return False


def logout():
    print("Exiting user")


def load_tasks():
    print("Loading tasks")


def main():
    input_login_id = input("What is your userID?")
    if (attempt_login(input_login_id)):
        print(
            f"Welcome back {current_user_first_name} {current_user_last_name}")
    else:
        print("Welcome new user!")

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
