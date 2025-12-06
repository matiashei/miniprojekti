import unittest

from unittest.mock import Mock
from services.bibtex_service import BibtexService

class TestBibtexService(unittest.TestCase):
    def setUp(self):
        citation_repo = Mock()
        self.bibtex_service = BibtexService(citation_repo)

    def test_get_book_bibtex(self):
        citation = Mock()
        citation.author = "Matti Meikalainen"
        citation.title = "Testikirja"
        citation.year = "2020"
        citation.publisher = "Testijulkaisija"
        citation.isbn = "123-4567890123"

        result = self.bibtex_service.get_book_bibtex(citation, 1)

        expected = (
            "@book{book1,\n"
            "    author = {Matti Meikalainen},\n"
            "    title = {Testikirja},\n"
            "    year = {2020},\n"
            "    publisher = {Testijulkaisija},\n"
            "    isbn = {123-4567890123}\n"
            "}"
        )

        self.assertEqual(result, expected)

    def test_get_inproceedings_bibtex(self):
        citation = Mock()
        citation.author = "Matti Meikalainen"
        citation.title = "Testipaperi"
        citation.year = "2020"
        citation.booktitle = "Testiotsikko"

        result = self.bibtex_service.get_inproceedings_bibtex(citation, 1)

        expected = (
            "@inproceedings{inproceedings1,\n"
            "    author = {Matti Meikalainen},\n"
            "    title = {Testipaperi},\n"
            "    year = {2020},\n"
            "    booktitle = {Testiotsikko}\n"
            "}"
        )

        self.assertEqual(result, expected)

    def test_get_article_bibtex(self):
        citation = Mock()
        citation.author = "Matti Meikalainen"
        citation.title = "Testiartikkeli"
        citation.year = "2020"
        citation.journal = "Testilehti"

        result = self.bibtex_service.get_article_bibtex(citation, 1)
        expected = (
            "@article{article1,\n"
            "    author = {Matti Meikalainen},\n"
            "    title = {Testiartikkeli},\n"
            "    journal = {Testilehti},\n"
            "    year = {2020}\n"
            "}"
        )

        self.assertEqual(result, expected)
