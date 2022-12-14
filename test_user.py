import unittest

from user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        # Create a test user before beginning each test
        self.user1 = User("John", "Smith")

    def tearDown(self):
        # Delete the test user after completing each test
        del self.user1

    # TODO: Create test cases for User creation

    # Tests first name reassignment
    def test_set_first_name(self):

        # First Name Reassignment to Nonempty String
        self.user1.set_first_name("Bob")
        self.assertEqual(self.user1.first_name, "Bob")

        # First Name Reassignment to Empty String
        self.assertRaises(Exception, self.user1.set_first_name, "")

        # First Name Reassignment to Short String
        self.assertRaises(Exception, self.user1.set_first_name, "a")

        # First Name Reassignment to Numbers Only String
        self.assertRaises(Exception, self.user1.set_first_name, "123")

        # First Name Reassignment to Mix Numbers and Letters String
        self.assertRaises(Exception, self.user1.set_first_name, "a23")

        # First Name Reassignment to Int Type
        self.assertRaises(Exception, self.user1.set_first_name, 5)

        # First Name Reassignment to None Type
        self.assertRaises(Exception, self.user1.set_first_name, None)

    # Tests last name reassignment
    def test_set_last_name(self):
        # Last Name Reassignment to Nonempty String Failed
        self.user1.set_last_name("Bob")
        self.assertEqual(self.user1.last_name, "Bob")

        # Last Name Reassignment to Empty String"
        self.assertRaises(Exception, self.user1.set_last_name, "")

        # Last Name Reassignment to Short String
        self.assertRaises(Exception, self.user1.set_last_name, "a")

        # Last Name Reassignment to Numbers Only String
        self.assertRaises(Exception, self.user1.set_last_name, "123")

        # Last Name Reassignment to Mix Numbers and Letters String
        self.assertRaises(Exception, self.user1.set_last_name, "a23")

        # Last Name Reassignment to Int Type
        self.assertRaises(Exception, self.user1.set_last_name, 5)

        # Last Name Reassignment to None Type
        self.assertRaises(Exception, self.user1.set_last_name, None)


if __name__ == "__main__":
    unittest.main()
