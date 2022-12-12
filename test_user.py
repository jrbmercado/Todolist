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
        self.user1.set_first_name("Bob")
        self.assertEqual(self.user1.first_name, "Bob",
                         msg="First Name Reassignment to Nonempty String Failed")
        self.assertRaises(Exception, self.user1.set_first_name, "",
                          msg="First Name Reassignment to Empty String Error Not Thrown")
        self.assertRaises(Exception, self.user1.set_first_name, "a",
                          msg="First Name Reassignment to Short String Error Not Thrown")
        self.assertRaises(Exception, self.user1.set_first_name, "123",
                          msg="First Name Reassignment to Numbers Only String Error Not Thrown")
        self.assertRaises(Exception, self.user1.set_first_name, "a23",
                          msg="First Name Reassignment to Mix Numbers and Letters String Error Not Thrown")
        self.assertRaises(Exception, self.user1.set_first_name, 5,
                          msg="First Name Reassignment to Int Type Error Not Thrown")
        self.assertRaises(Exception, self.user1.set_first_name, None,
                          msg="First Name Reassignment to None Type Error Not Thrown")

    # Tests last name reassignment
    def test_set_last_name(self):
        self.user1.set_last_name("Bob")
        self.assertEqual(self.user1.last_name, "Bob",
                         msg="Last Name Reassignment to Nonempty String Failed")
        self.assertRaises(Exception, self.user1.set_last_name, "",
                          msg="Last Name Reassignment to Empty String Error Not Thrown")
        self.assertRaises(Exception, self.user1.set_last_name, "a",
                          msg="Last Name Reassignment to Short String Error Not Thrown")
        self.assertRaises(Exception, self.user1.set_last_name, "123",
                          msg="Last Name Reassignment to Numbers Only String Error Not Thrown")
        self.assertRaises(Exception, self.user1.set_last_name, "a23",
                          msg="Last Name Reassignment to Mix Numbers and Letters String Error Not Thrown")
        self.assertRaises(Exception, self.user1.set_last_name, 5,
                          msg="Last Name Reassignment to Int Type Error Not Thrown")
        self.assertRaises(Exception, self.user1.set_last_name, None,
                          msg="Last Name Reassignment to None Type Error Not Thrown")


if __name__ == "__main__":
    unittest.main()
