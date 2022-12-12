class User:
    # Constructor that accepts first and last name, ID and taskboard is auto filled by program
    def __init__(self, firstName, lastName):
        # Set firstname an lastname to input values
        self.firstName = firstName
        self.lastName = lastName
        # TODO: Create Unique ID's for each user, for database access
        self.id = 0
        # Initialize taskboard to empty array of tasks
        self.taskBoard = []

    # Prints object as first and last name and userID. Tasks in task board will not be displayed.
    # TODO: Create tasks in taskboard to be displayed if object is requested to be printed
    def __str__(self):
        return f"Name: {self.firstName} {self.lastName} \n UserID: {self.id}"

    # Reassigns first name to a different first name
    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    # Reassigns last name to a different last name
    def setLastName(self, newLastName):
        self.lastName = newLastName
