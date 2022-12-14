import datetime


class Task:
    def __init__(self, title="Title", detail="Detail", due_date=datetime.datetime.today(), creation_date=datetime.datetime.today(), completed=False):
        self.title = title
        self.detail = detail
        self.due_date = due_date
        self.creation_date = creation_date
        self.completed = completed

    def set_title(self, title):
        if (title is None or title == ""):
            raise Exception("Title cannot be empty")
        elif (isinstance(title, str)):
            self.title = title
        else:
            self.title = str(title)

    def set_detail(self, detail):
        if (detail is None):
            self.detail = ""
        elif (isinstance(detail, str)):
            self.detail = detail
        else:
            self.detail = str(detail)

    def set_due_date(self, due_date):
        if (due_date is not None and
           due_date.date() >= self.creation_date.date() and
           isinstance(due_date, datetime.datetime)):
            self.due_date = due_date
        else:
            raise Exception(
                "Due Date cannot be in the past and must be a valid date")

    def set_creation_date(self, creation_date):
        if (creation_date is not None and
            creation_date.date() <= self.creation_date.date() and
                isinstance(creation_date, datetime.datetime)):
            self.creation_date = creation_date
        else:
            raise Exception(
                "Creation Date cannot be in the future and must be a valid date")

    def set_completed(self, completed):
        if (isinstance(completed, bool)):
            self.completed = completed
        else:
            raise Exception("Completed status must be True or False")
