import unittest

from unittest.mock import Mock
from services.bibtex_service import BibtexService
from entities.citation import Citation

class TestBibtexService(unittest.TestCase):
    def setUp(self):
        self.citation_repo = Mock()
        self.bibtex_service = BibtexService(self.citation_repo)

    def test_get_book_bibtex(self):
        citation = Citation(
            citation_id = 1,
            citation_type = "book",
            title = "Testikirja",
            author = "Matti Meikalainen",
            publisher = "Testijulkaisija",
            isbn = "123-4567890123",
            year = "2020",
            booktitle = None,
            journal = None,
        )

        self.citation_repo.get_citation.return_value = citation
        result = self.bibtex_service.get_bibtex_citation(1)

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
        citation = Citation(
            citation_id = 1,
            citation_type = "inproceedings",
            title = "Testipaperi",
            author = "Matti Meikalainen",
            publisher = None,
            isbn = None,
            year = "2020",
            booktitle = "Testiotsikko",
            journal = None,
        )

        self.citation_repo.get_citation.return_value = citation
        result = self.bibtex_service.get_bibtex_citation(1)

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
        citation = Citation(
            citation_id = 1,
            citation_type = "article",
            title = "Testiartikkeli",
            author = "Matti Meikalainen",
            publisher = None,
            isbn = None,
            year = "2020",
            booktitle = None,
            journal = "Testilehti",
        )

        self.citation_repo.get_citation.return_value = citation
        result = self.bibtex_service.get_bibtex_citation(1)

        expected = (
            "@article{article1,\n"
            "    author = {Matti Meikalainen},\n"
            "    title = {Testiartikkeli},\n"
            "    journal = {Testilehti},\n"
            "    year = {2020}\n"
            "}"
        )

        self.assertEqual(result, expected)

    def test_no_bibtex_for_invalid_citation(self):
        self.citation_repo.get_citation.return_value = None

        result = self.bibtex_service.get_bibtex_citation(999)

        self.assertIsNone(result)

    def test_no_bibtex_for_invalid_citation_type(self):
        citation = Mock()
        citation.type = "INVALID_TYPE"
        self.citation_repo.get_citation.return_value = citation

        result = self.bibtex_service.get_bibtex_citation(1)

        self.assertIsNone(result)
