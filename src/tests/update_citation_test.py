import unittest
from unittest.mock import Mock, patch
from werkzeug.datastructures import MultiDict

from repositories.citation_repository import CitationRepository
from services.citation_service import CitationService

class TestUpdateCitation(unittest.TestCase):
    def setUp(self):
        self.citation_repo = CitationRepository(Mock())
        self.citation_service = CitationService(self.citation_repo, Mock(), Mock())

        self.book_citation = MultiDict({
            "title": "Testikirja",
            "author": "Matti Meikalainen",
            "publisher": "Testijulkaisija",
            "isbn": "123-4567890123",
            "year": "2025"
        })
        self.inproceedings_citation = MultiDict({
            "title": "Testipaperi",
            "author": "Matti Meikalainen",
            "booktitle": "Testiotsikko",
            "year": "2025"
        })
        self.article_citation = MultiDict({
            "title": "Testiartikkeli",
            "author": "Matti Meikalainen",
            "journal": "Testilehti",
            "year": "2025",
            "tags": "tag1, tag2"
        })

    @patch("repositories.citation_repository.db")
    def test_update_one_book_citation(self, mock_db):
        self.citation_service.update_citation(1, "book", self.book_citation)

        mock_db.session.execute.assert_called_once()
        mock_db.session.commit.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_update_one_article_citation(self, mock_db):
        self.citation_service.update_citation(1, "article", self.article_citation)

        mock_db.session.execute.assert_called_once()
        mock_db.session.commit.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_update_one_inproceedings_citation(self, mock_db):
        self.citation_service.update_citation(1, "inproceedings", self.inproceedings_citation)

        mock_db.session.execute.assert_called_once()
        mock_db.session.commit.assert_called_once()
