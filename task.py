import datetime


class Task:
    def __init__(self, title="Title", detail="Detail", due_date=datetime.datetime.today(), created_date=datetime.datetime.today(), completed=False):
        self.title = title
        self.detail = detail
        self.due_date = due_date
        self.created_date = created_date
        self.completed = completed

    def set_title(self, title):
        if (title is not None and
                title != ""):
            self.title = title
        else:
            raise Exception("Title cannot be empty")

    def set_detail(self, detail):
        if (detail is not None):
            self.detail = detail
        else:
            self.detail = ""

    def set_due_date(self, due_date):
        if (due_date is not None and
           due_date.date() > self.created_date.date() and
           type(due_date) == datetime.datetime):
            self.due_date = due_date
        else:
            raise Exception(
                "Due Date cannot be in the past and must be a valid date")

    def set_creation_date(self, created_date):
        if (created_date is not None and
            created_date.date() < self.created_date.date() and
           type(created_date) == datetime.datetime):
            self.created_date = created_date
        else:
            raise Exception(
                "Creation Date cannot be in the future and must be a valid date")

    def set_completed(self, completed):
        if (type(completed) == bool):
            self.completed = completed
        else:
            raise Exception("Completed status must be True or False")
