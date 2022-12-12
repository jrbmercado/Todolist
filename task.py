import datetime


class Task:
    def __init__(self, title="Title", detail="Detail", due_date=datetime.datetime.today(), created_date=datetime.datetime.today(), completed=False):
        self.title = title
        self.detail = detail
        self.due_date = due_date
        self.created_date = created_date
        self.completed = completed
