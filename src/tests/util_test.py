import unittest

from attr import validate
from util import validate_book, UserInputError

class TestValidateBook(unittest.TestCase):

    def test_valid_book(self):
        validate_book("Title", "Author", "Pub", "12345", "2025")

    def test_empty_title(self):
        with self.assertRaises(UserInputError):
            validate_book("", "Author", "Publisher", "123", "2025")

    def test_title_is_space(self):
        with self.assertRaises(UserInputError):
            validate_book(" ", "Author", "Publisher", "123", "2025")

    def test_too_long_title(self):
        with self.assertRaises(UserInputError):
            validate_book("x" * 200, "Author", "Publisher", "123", "2025")

    def test_author_is_space(self):
        with self.assertRaises(UserInputError):
            validate_book("Title", " ", "Publisher", "123", "2025")

    def test_too_long_author(self):
        with self.assertRaises(UserInputError):
            validate_book("Title", "x" * 76, "Publisher", "123", "2025")

    def test_publisher_is_space(self):
        with self.assertRaises(UserInputError):
            validate_book("Title", "Author", " ", "123", "2025")

    def test_too_long_publisher(self):
        with self.assertRaises(UserInputError):
            validate_book("Title", "Author", "x" * 51, "123", "2025")

    def test_isbn_is_space(self):
        with self.assertRaises(UserInputError):
            validate_book("Title", "Author", "Publisher", " ", "2025")

    def test_too_long_isbn(self):
        with self.assertRaises(UserInputError):
            validate_book("Title", "Author", "Publisher", "0" * 21, "2025")

    def test_year_is_space(self):
        with self.assertRaises(UserInputError):
            validate_book("Title", "Author", "Publisher", "123", " ")

    def test_too_high_year(self):
        with self.assertRaises(UserInputError):
            validate_book("Title", "Author", "Publisher", "123", "2026")

    def test_too_low_year(self):
        with self.assertRaises(UserInputError):
            validate_book("Title", "Author", "Publisher", "123", "-1")
            