from task import Task
from user import User
import traceback

class Todo_Engine():
    def __init__(self, user_id="-1", first_name="fName", last_name="lName"):
        self.current_user_id = user_id
        self.current_first_name = first_name
        self.current_last_name = last_name

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
                if(lineContents[0] == user_id): # If they match, update object attributes to match name in database
                    self.current_user_id = user_id # Update user_id to the one attempting to log in successfully
                    self.current_first_name = lineContents[1].capitalize() # Update first name and capitalize first letter
                    self.current_last_name = lineContents[2].capitalize() # Update last name and capitalize first letter
                    return True # Return true, indicating a successful login and reassignment of object attributes
        return False # Return false that a login was unsuccessful due to error or user not found in database

    def login(self):
        # Request for the user_id of the person using application
        input_login_id = input("What is your userID? ")
        # Attempt to find user_id in database
        if(self.found_user_info(input_login_id)): # If successful, greet user back
            print(f"Welcome back {self.current_first_name} {self.current_last_name}")
        else: # If unsuccessful we need to get more info and add them to the database
            # TODO: Call create_new_user() function
            print("Welcome new user! Let's create a new account.")
            self.create_new_user()

    # TODO: Create a function that gathers user first name, last name, and user ID, then writes info to user_database.txt for future logins. Will be called by login if login is unsuccessful and user does not exist in database yet.
    def create_new_user(self):
        newUser = User()
        successful_fName_setup = False
        successful_lName_setup = False
        
        while(not successful_fName_setup):
            try:
                input_fName = input("What is your first name? ")
                newUser.set_first_name(input_fName)
                successful_fName_setup = True
            except Exception:
                print("First name input is not valid")

        while(not successful_lName_setup):
            try: 
                input_lName = input("What is your last name? ")
                newUser.set_last_name(input_lName)
                successful_lName_setup = True
            except Exception:
                print("Last name input is not valid")

        print(f"Created new user account for {newUser.first_name.capitalize()} {newUser.last_name.capitalize()}")

def main():
    test1 = Todo_Engine()
    test1.login()

if(__name__ == "__main__"):
    main()
