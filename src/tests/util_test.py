import unittest

from util import UserInputError, validate_book, validate_inproceedings, validate_article

class TestValidateBook(unittest.TestCase):

    def test_valid_book(self):
        validate_book("Title", "Author", "Publisher", "12345", "2025")

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


class TestValidateInproceedings(unittest.TestCase):

    def test_valid_inproceedings(self):
        validate_inproceedings("Title", "Author", "Book Title", "2025")

    def test_empty_title(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("", "Author", "Book Title", "2025")

    def test_title_is_space(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings(" ", "Author", "Book Title", "2025")

    def test_too_long_title(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("x" * 200, "Author", "Book Title", "2025")

    def test_author_is_space(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("Title", " ", "Book Title", "2025")

    def test_too_long_author(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("Title", "x" * 76, "Book Title", "2025")

    def test_boobktitle_is_space(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("Title", "Author", " ", "2025")

    def test_too_long_booktitle(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("Title", "Author", "x" * 76, "2025")

    def test_year_is_space(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("Title", "Author", "Booktitle", " ")

    def test_too_high_year(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("Title", "Author", "Booktitle", "2026")

    def test_too_low_year(self):
        with self.assertRaises(UserInputError):
            validate_inproceedings("Title", "Author", "Booktitle", "-1")


class TestValidateArticle(unittest.TestCase):

    def test_valid_article(self):
        validate_article("Title", "Author", "Journal", "2025")

    def test_empty_title(self):
        with self.assertRaises(UserInputError):
            validate_article("", "Author", "Journal", "2025")

    def test_title_is_space(self):
        with self.assertRaises(UserInputError):
            validate_article(" ", "Author", "Journal", "2025")

    def test_too_long_title(self):
        with self.assertRaises(UserInputError):
            validate_article("x" * 200, "Author", "Journal", "2025")

    def test_author_is_space(self):
        with self.assertRaises(UserInputError):
            validate_article("Title", " ", "Journal", "2025")

    def test_too_long_author(self):
        with self.assertRaises(UserInputError):
            validate_article("Title", "x" * 76, "Journal", "2025")

    def test_journal_is_space(self):
        with self.assertRaises(UserInputError):
            validate_article("Title", "Author", " ", "2025")

    def test_too_long_journal(self):
        with self.assertRaises(UserInputError):
            validate_article("Title", "Author", "x" * 76, "2025")

    def test_year_is_space(self):
        with self.assertRaises(UserInputError):
            validate_article("Title", "Author", "Journal", " ")

    def test_too_high_year(self):
        with self.assertRaises(UserInputError):
            validate_article("Title", "Author", "Journal", "2026")

    def test_too_low_year(self):
        with self.assertRaises(UserInputError):
            validate_article("Title", "Author", "Journal", "-1")
