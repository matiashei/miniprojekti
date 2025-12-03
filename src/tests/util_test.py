import unittest
from util import UserInputError, validate_book, validate_inproceedings, validate_article

VALID_BOOK = {
    "title": "Computer Organization and Architecture",
    "author": "William Stallings",
    "publisher": "Pearson",
    "isbn": "978-0-13-410161-3",
    "year": "2024"
}

VALID_INPROCEEDINGS = {
    "title": "A Conference Paper",
    "author": "John Doe",
    "booktitle": "Proceedings of a Conference",
    "year": "1996"
}

VALID_ARTICLE = {
    "title": "A Valid Article",
    "author": "Jane Smith",
    "journal": "Journal of Testing",
    "year": "3"
}

class TestValidateUtil(unittest.TestCase):

    def check_invalid(self, validation_func, base_kwargs, override_kwargs):
        test_kwargs = base_kwargs.copy()
        test_kwargs.update(override_kwargs)
        with self.assertRaises(UserInputError):
            validation_func(**test_kwargs)

    def test_valid_item(self):
        validate_book(**VALID_BOOK)
        validate_inproceedings(**VALID_INPROCEEDINGS)
        validate_article(**VALID_ARTICLE)

    def test_empty_title(self):
        self.check_invalid(validate_book, VALID_BOOK, {"title": ""})
        self.check_invalid(validate_inproceedings, VALID_INPROCEEDINGS, {"title": ""})
        self.check_invalid(validate_article, VALID_ARTICLE, {"title": ""})

    def test_too_long_title(self):
        self.check_invalid(validate_book, VALID_BOOK, {"title": "x" * 200})
        self.check_invalid(validate_inproceedings, VALID_INPROCEEDINGS, {"title": "x" * 200})
        self.check_invalid(validate_article, VALID_ARTICLE, {"title": "x" * 200})

    def test_empty_author(self):
        self.check_invalid(validate_book, VALID_BOOK, {"author": ""})
        self.check_invalid(validate_inproceedings, VALID_INPROCEEDINGS, {"author": ""})
        self.check_invalid(validate_article, VALID_ARTICLE, {"author": ""})

    def test_negative_year(self):
        self.check_invalid(validate_book, VALID_BOOK, {"year": "-5"})
        self.check_invalid(validate_inproceedings, VALID_INPROCEEDINGS, {"year": "-5"})
        self.check_invalid(validate_article, VALID_ARTICLE, {"year": "-5"})

    def test_too_high_year(self):
        self.check_invalid(validate_book, VALID_BOOK, {"year": "3000"})
        self.check_invalid(validate_inproceedings, VALID_INPROCEEDINGS, {"year": "3000"})
        self.check_invalid(validate_article, VALID_ARTICLE, {"year": "3000"})

    def test_invalid_publisher(self):
        self.check_invalid(validate_book, VALID_BOOK, {"publisher": "   "})
        self.check_invalid(validate_book, VALID_BOOK, {"publisher": ""})
        self.check_invalid(validate_book, VALID_BOOK, {"publisher": "x" * 100})

    def test_invalid_isbn(self):
        self.check_invalid(validate_book, VALID_BOOK, {"isbn": ""})
        self.check_invalid(validate_book, VALID_BOOK, {"isbn": "   "})
        self.check_invalid(validate_book, VALID_BOOK, {"isbn": "x" * 50})

    def test_invalid_booktitle(self):
        self.check_invalid(validate_inproceedings, VALID_INPROCEEDINGS, {"booktitle": ""})
        self.check_invalid(validate_inproceedings, VALID_INPROCEEDINGS, {"booktitle": "   "})
        self.check_invalid(validate_inproceedings, VALID_INPROCEEDINGS, {"booktitle": "x" * 100})

    def test_invalid_journal(self):
        self.check_invalid(validate_article, VALID_ARTICLE, {"journal": ""})
        self.check_invalid(validate_article, VALID_ARTICLE, {"journal": "   "})
        self.check_invalid(validate_article, VALID_ARTICLE, {"journal": "x" * 100})