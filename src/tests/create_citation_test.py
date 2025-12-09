import unittest
from unittest.mock import Mock, patch, ANY
from werkzeug.datastructures import MultiDict

from repositories.citation_repository import CitationRepository
from services.citation_service import CitationService

class TestCreateCitation(unittest.TestCase):
    def setUp(self):
        self.book_citation = MultiDict({
            "title": "Testikirja",
            "author": "Matti Meikalainen",
            "publisher": "Testijulkaisija",
            "isbn": "123-4567890123",
            "year": "2023"
        })
        self.inproceedings_citation = MultiDict({
            "title": "Testipaperi",
            "author": "Matti Meikalainen",
            "booktitle": "Testiotsikko",
            "year": "2023"
        })
        self.article_citation = MultiDict({
            "title": "Testiartikkeli",
            "author": "Matti Meikalainen",
            "journal": "Testilehti",
            "year": "2023"
        })

        self.citation_repo = CitationRepository(Mock())
        self.citation_service = CitationService(self.citation_repo, Mock(), Mock())

    @patch("repositories.citation_repository.db")
    def test_create_valid_book_citation(self, mock_db):
        self.citation_service.create_citation("book", self.book_citation)

        mock_db.session.execute.assert_called_once_with(ANY, {
            "citation_type": "book",
            "title": self.book_citation["title"],
            "author": self.book_citation["author"],
            "publisher": self.book_citation["publisher"],
            "isbn": self.book_citation["isbn"],
            "year": self.book_citation["year"]
            }
        )
        mock_db.session.commit.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_create_valid_inproceedings_citation(self, mock_db):
        self.citation_service.create_citation("inproceedings", self.inproceedings_citation)

        mock_db.session.execute.assert_called_once_with(ANY, {
            "citation_type": "inproceedings",
            "title": self.inproceedings_citation["title"],
            "author": self.inproceedings_citation["author"],
            "booktitle": self.inproceedings_citation["booktitle"],
            "year": self.inproceedings_citation["year"]
            }
        )
        mock_db.session.commit.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_create_valid_article_citation(self, mock_db):
        self.citation_service.create_citation("article", self.article_citation)

        mock_db.session.execute.assert_called_once_with(ANY, {
            "citation_type": "article",
            "title": self.article_citation["title"],
            "author": self.article_citation["author"],
            "journal": self.article_citation["journal"],
            "year": self.article_citation["year"]
            }
        )
        mock_db.session.commit.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_create_consecutive_citations(self, mock_db):
        self.citation_service.create_citation("book", self.book_citation)
        self.citation_service.create_citation("article", self.article_citation)
        self.citation_service.create_citation("inproceedings", self.inproceedings_citation)

        self.assertEqual(mock_db.session.execute.call_count, 3)

    def test_citation_not_created_with_invalid_type(self):
        with self.assertRaises(ValueError):
            self.citation_service.create_citation("invalid_type", self.book_citation)
