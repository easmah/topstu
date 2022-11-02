import unittest
from Testing.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py"""

    def test_first_last_name(self):
        """Does name like Jason Noah work"""
        formatted_name = get_formatted_name('Jason', 'Noah')
        self.assertEqual(formatted_name, 'Jason Noah')


if __name__ == '__main__':
    unittest.main()

