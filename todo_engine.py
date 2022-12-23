from task import Task
from user import User
import traceback


class Todo_Engine():
    def __init__(self, user_id="-1", first_name="fName", last_name="lName"):
        self.current_user_id = user_id
        self.current_first_name = first_name
        self.current_last_name = last_name
        self.tasks = []

    def found_user_info(self, user_id):
        # Context manager to attempt to open user_database.txt
        with open("user_database.txt", "r") as opened_user_database:
            # Read the lines in the database and seperate by new line characters
            lines = opened_user_database.read().splitlines()
            # For each line of the file
            for line in lines:
                # Seperate each entry by commas
                lineContents = line.split(",")
                # Check to see if the first entry which is the user_id, matches the user_id attempting to log in
                # If they match, update object attributes to match name in database
                if (lineContents[0] == user_id):
                    # Update user_id to the one attempting to log in successfully
                    self.current_user_id = user_id
                    # Update first name and capitalize first letter
                    self.current_first_name = lineContents[1].capitalize()
                    # Update last name and capitalize first letter
                    self.current_last_name = lineContents[2].capitalize()
                    return True  # Return true, indicating a successful login and reassignment of object attributes
        return False  # Return false that a login was unsuccessful due to error or user not found in database

    def login(self):
        # Request for the user_id of the person using application
        input_login_id = input("What is your userID? ")
        # Attempt to find user_id in database
        if (self.found_user_info(input_login_id)):  # If successful, greet user back
            print(
                f"Welcome back {self.current_first_name} {self.current_last_name}")
            self.loadTasks(input_login_id)
        else:  # If unsuccessful we need to get more info and add them to the database
            # TODO: Call create_new_user() function
            print("Welcome new user! Let's create a new account.")
            self.create_new_user(input_login_id)

    # TODO: Create a function that gathers user first name, last name, and user ID, then writes info to user_database.txt for future logins. Will be called by login if login is unsuccessful and user does not exist in database yet.
    def create_new_user(self, input_login_id):
        newUser = User()
        newUser.id = input_login_id
        successful_fName_setup = False
        successful_lName_setup = False

        while (not successful_fName_setup):
            try:
                input_fName = input("What is your first name? ")
                newUser.set_first_name(input_fName)
                successful_fName_setup = True
            except Exception:
                print("First name input is not valid")

        while (not successful_lName_setup):
            try:
                input_lName = input("What is your last name? ")
                newUser.set_last_name(input_lName)
                successful_lName_setup = True
            except Exception:
                print("Last name input is not valid")

        with open("user_database.txt", "a") as opened_user_database:
            opened_user_database.write(
                f"\n{newUser.id},{newUser.first_name},{newUser.last_name}")

        print(
            f"Created new user account for {newUser.first_name.capitalize()} {newUser.last_name.capitalize()}")

        self.loadTasks(newUser.id)

    def loadTasks(self, user_id):
        with open("task_database.txt", "r") as opened_task_database:
            # Read the lines in the database and seperate by new line characters
            lines = opened_task_database.read().splitlines()
            # For each line of the file
            for line in lines:
                # Seperate each entry by commas
                lineContents = line.split(",")
                # Check to see if the first entry which is the owner_id, matches the user_id that is logged in
                # If they match, add the task to the opened
                if (lineContents[0] == user_id):
                    newTask = Task(lineContents[1], lineContents[2])
                    # print(f"Added new task {newTask.title} {newTask.detail}")
                    self.tasks.append(newTask)
            # print("Tasks loaded")
            self.menu()

    def viewTasks(self):
        count = 0
        for task in self.tasks:
            count += 1
            print(f"{count} - {task.title} \n \t{task.detail}")
        self.menu()

    def menu(self):
        print("="*30)
        print("0 = View all tasks")
        inputChoice = input("Please select an option: ")
        print("="*30)

        match inputChoice:
            case "0":
                self.viewTasks()


def main():
    test1 = Todo_Engine()
    test1.login()


if (__name__ == "__main__"):
    main()
