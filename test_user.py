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
    def test_setFirstName(self):
        self.user1.setFirstName("Bob")
        self.assertEqual(self.user1.firstName, "Bob",
                         msg="First Name Reassignment to Nonempty String Failed")
        self.assertRaises(Exception, self.user1.setFirstName, "",
                          msg="First Name Reassignment to Empty String Error Not Thrown")
        self.assertRaises(Exception, self.user1.setFirstName, "a",
                          msg="First Name Reassignment to Short String Error Not Thrown")
        self.assertRaises(Exception, self.user1.setFirstName, "123",
                          msg="First Name Reassignment to Numbers Only String Error Not Thrown")
        self.assertRaises(Exception, self.user1.setFirstName, "a23",
                          msg="First Name Reassignment to Mix Numbers and Letters String Error Not Thrown")
        self.assertRaises(Exception, self.user1.setFirstName, 5,
                          msg="First Name Reassignment to Int Type Error Not Thrown")
        self.assertRaises(Exception, self.user1.setFirstName, None,
                          msg="First Name Reassignment to None Type Error Not Thrown")

    # Tests last name reassignment
    def test_setLastName(self):
        self.user1.setLastName("Bob")
        self.assertEqual(self.user1.lastName, "Bob",
                         msg="Last Name Reassignment to Nonempty String Failed")
        self.assertRaises(Exception, self.user1.setLastName, "",
                          msg="Last Name Reassignment to Empty String Error Not Thrown")
        self.assertRaises(Exception, self.user1.setLastName, "a",
                          msg="Last Name Reassignment to Short String Error Not Thrown")
        self.assertRaises(Exception, self.user1.setLastName, "123",
                          msg="Last Name Reassignment to Numbers Only String Error Not Thrown")
        self.assertRaises(Exception, self.user1.setLastName, "a23",
                          msg="Last Name Reassignment to Mix Numbers and Letters String Error Not Thrown")
        self.assertRaises(Exception, self.user1.setLastName, 5,
                          msg="Last Name Reassignment to Int Type Error Not Thrown")
        self.assertRaises(Exception, self.user1.setLastName, None,
                          msg="Last Name Reassignment to None Type Error Not Thrown")


if __name__ == "__main__":
    unittest.main()
