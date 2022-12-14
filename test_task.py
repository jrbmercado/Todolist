import unittest

from task import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        # Create a test task before beginning each test
        self.task1 = Task("TitleTask", "DetailTask")

    def tearDown(self):
        # Delete the test user after completing each test
        del self.task1

    def test_set_title(self):

        # Title Reassignment to Nonempty String
        self.task1.set_title("NewTitle")
        self.assertEqual(self.task1.title, "NewTitle")

        # Title Reassignment to Empty Type Error Not Thrown
        self.assertRaises(Exception, self.task1.set_title, None)


if __name__ == "__main__":
    unittest.main()
