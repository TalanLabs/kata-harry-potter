import unittest


class HarryPotter(unittest.TestCase):
    def test_foo(self):
        self.assertEqual("foo", "foo")


if __name__ == '__main__':
    unittest.main()
