import datetime


class Task:
    def __init__(self, title="Title", detail="Detail", due_date=datetime.datetime.today(), creation_date=datetime.datetime.today(), completed=False):
        # Set Title and Detail to inputs
        self.title = title
        self.detail = detail
        # Auto fill due date, creation date, and completed status if not passed in constructor
        self.due_date = due_date
        self.creation_date = creation_date
        self.completed = completed

    # Reassign title to a different title with error checking
    def set_title(self, title):
        if (title is None or title == ""): # If title is empty, throw exception, title cannot be blank
            raise Exception("Title cannot be empty")
        elif (isinstance(title, str)): # If title is a valid string, reassign detail
            self.title = title
        else:
            self.title = str(title) # If title is a different data type, typecase into string, then reassign title

    # Reassign detail to a different detail with error checking
    def set_detail(self, detail):
        if (detail is None): # If detail is empty, just set as empty string, OK
            self.detail = ""
        elif (isinstance(detail, str)): # If detail is a valid string, reassign detail
            self.detail = detail
        else:
            self.detail = str(detail) # If detail is different data type, typecast into string, then reassign detail

    # Reassign due date to a different due date with error checking
    def set_due_date(self, due_date):
        if (due_date is not None and
           due_date.date() >= self.creation_date.date() and
           isinstance(due_date, datetime.datetime)): # If new due date is not none AND new due date is today or a future date AND new due date is a datetime type
            self.due_date = due_date # Reassign due date
        else: # Otherwise, one or multiple of the requirements are not met and throw exception
            raise Exception(
                "Due Date cannot be in the past and must be a valid date")

    # Reassign creation date to a different creation date with error checking
    def set_creation_date(self, creation_date):
        if (creation_date is not None and
            creation_date.date() <= self.creation_date.date() and
                isinstance(creation_date, datetime.datetime)): # If new creation date is not none AND new creation date is today or a past date AND new creation date is a datetime type
            self.creation_date = creation_date # Reassign creation date
        else: # Otherwise, one or multiple of the requirements are not met and throw exception
            raise Exception(
                "Creation Date cannot be in the future and must be a valid date")

    # Reassign completed status to a different state of True or False with error checking
    def set_completed(self, completed):
        if (isinstance(completed, bool)): # If completed status is a boolean type
            self.completed = completed # Reassign completed status
        else: # Otherwise, throw exception
            raise Exception("Completed status must be True or False")
