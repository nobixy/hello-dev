import unittest

from hello import greet


class GreetingTest(unittest.TestCase):
    def test_greets_the_given_name(self):
        self.assertEqual(greet("Joe"), "Hello, Joe! Welcome to the dev server.")


if __name__ == "__main__":
    unittest.main()
