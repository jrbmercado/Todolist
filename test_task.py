import unittest
from datetime import datetime, timedelta

from task import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        # Create test tasks before beginning each test
        # Current Date Reassignment Testing / Error Checks Testing
        self.task1 = Task("TitleTask", "DetailTask")
        # Past Date Reassignment Testing
        self.task2 = Task("TitleTask", "DetailTask")
        # Future Date Reassignment Testing
        self.task3 = Task("TitleTask", "DetailTask")

    def tearDown(self):
        # Delete test tasks after completing each test
        del self.task1
        del self.task2
        del self.task3

    def test_set_title(self):

        # Title Reassignment to None Type
        self.assertRaises(Exception, self.task1.set_title, None)

        # Title Reassignment to Nonempty String
        self.task1.set_title("NewTitle")
        self.assertEqual(self.task1.title, "NewTitle")

        # Title Reassignment to Empty String
        self.assertRaises(Exception, self.task1.set_title, "")

        # Title Reassignment to Int Type
        self.task1.set_title(123)
        self.assertEqual(self.task1.title, "123")

    def test_set_detail(self):

        # Detail Reassignment to None Type
        self.task1.set_detail(None)
        self.assertEqual(self.task1.detail, "")

        # Detail Reassignment to Nonempty String
        self.task1.set_detail("NewDetail")
        self.assertEqual(self.task1.detail, "NewDetail")

        # Detail Reassignment to Empty String
        self.task1.set_detail("")
        self.assertEqual(self.task1.detail, "")

        # Detail Reassignment to Int Type
        self.task1.set_detail(123)
        self.assertEqual(self.task1.detail, "123")

    def test_set_due_date(self):
        # Current Date to use for tests
        current_date = datetime.today()

        # Due Date Reassignment to Current Date
        self.task1.set_due_date(current_date)
        self.assertEqual(self.task1.due_date, current_date)

        # Due Date Reassignment to None Type
        self.assertRaises(Exception, self.task1.set_due_date, None)

        # Due Date Reassignment to String Type
        self.assertRaises(Exception, self.task1.set_due_date, "RandomString")

        # Due Date Reassignment to Int Type
        self.assertRaises(Exception, self.task1.set_due_date, 123)

        # Due Date Reassignment to Past Date
        past_date = current_date-timedelta(days=1)
        self.assertRaises(Exception, self.task2.set_due_date, past_date)

        # Due Date Reassignment to Future Date
        future_date = current_date+timedelta(days=1)
        self.task3.set_due_date(future_date)
        self.assertEqual(self.task3.due_date, future_date)

    def test_set_creation_date(self):
        # Current Date to use for tests
        current_date = datetime.today()

        # Creation Date Reassignment to Current Date
        self.task1.set_creation_date(current_date)
        self.assertEqual(self.task1.creation_date, current_date)

        # Creation Date Reassignment to None Type
        self.assertRaises(Exception, self.task1.set_creation_date, None)

        # Creation Date Reassignment to String Type
        self.assertRaises(
            Exception, self.task1.set_creation_date, "RandomString")

        # Creation Date Reassignment to Int Type
        self.assertRaises(Exception, self.task1.set_creation_date, 123)

        # Creation Date Reassignment to Past Date
        past_date = current_date-timedelta(days=1)
        self.task2.set_creation_date(past_date)
        self.assertEqual(self.task2.creation_date, past_date)

        # Creation Date Reassignment to Future Date
        future_date = current_date+timedelta(days=1)
        self.assertRaises(Exception, self.task3.set_creation_date, future_date)

    def test_set_completed(self):
        # Completed Reassignment to None
        self.assertRaises(Exception, self.task1.set_completed, None)

        # Completed Reassignment to True
        self.task1.set_completed(True)
        self.assertEqual(self.task1.completed, True)

        # Competed Reassignemnt to False
        self.task1.set_completed(False)
        self.assertEqual(self.task1.completed, False)

        # Completed Reassignment to Int Type
        self.assertRaises(Exception, self.task1.set_completed, 123)

        # Completed Reassignemnt to String
        self.assertRaises(Exception, self.task1.set_completed, "RandomString")


if __name__ == "__main__":
    unittest.main()
