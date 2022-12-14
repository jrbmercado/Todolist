import re


class User:
    # Constructor that accepts first and last name, ID and taskboard is auto filled by program
    def __init__(self, first_name="First", last_name="Last"):
        # Set firstname an lastname to input values
        self.first_name = first_name
        self.last_name = last_name
        # TODO: Create Unique ID's for each user, for database access
        self.id = 0
        # Initialize taskboard to empty array of tasks
        self.task_board = []

    # Prints object as first and last name and userID. Tasks in task board will not be displayed.
    # TODO: Create tasks in taskboard to be displayed if object is requested to be printed
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} \n UserID: {self.id}"

    # Checks to see if a string contains a number
    def contains_number(self, value):
        numbers = re.findall('\d+', value)
        return True if numbers else False

    # Reassigns first name to a different first name with error checking
    # TODO: Add error check for special characters
    def set_first_name(self, new_first_name):
        if (
            isinstance(new_first_name, str) and
            self.contains_number(new_first_name) == False and
            len(new_first_name) >= 2
        ):
            self.first_name = new_first_name
        else:
            raise Exception(
                "First Name must be a valid string with at least 2 characters")

    # Reassigns last name to a different last name with error checking
    # TODO: Add error check for special characters
    def set_last_name(self, new_last_name):
        if (
            isinstance(new_last_name, str) and
            self.contains_number(new_last_name) == False and
            len(new_last_name) >= 2
        ):
            self.last_name = new_last_name
        else:
            raise Exception(
                "Last Name must be a valid string with at least 2 characters")
