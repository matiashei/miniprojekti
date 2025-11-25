import unittest

from unittest.mock import patch
from repositories.citation_repository import update_book_citation, update_article_citation, update_inproceedings_citation

class TestupdateCitation(unittest.TestCase):
    @patch("repositories.citation_repository.db")
    def test_update_one_book_citation(self, mock_db):
        update_book_citation(1, "title", "author", "publisher", "12345678", "2020")
        mock_db.session.execute.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_update_one_article_citation(self, mock_db):
        update_article_citation(1, "title", "author", "journal", "2020")
        mock_db.session.execute.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_update_one_inproceedings_citation(self, mock_db):
        update_inproceedings_citation(1, "title", "author", "booktitle", "2020")
        mock_db.session.execute.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_update_several_citations(self, mock_db):
        update_book_citation(1, "title", "author", "publisher", "12345678", "2020")
        update_book_citation(2, "title", "author", "publisher", "12345678", "2020")
        update_article_citation(3, "title", "author", "journal", "2020")
        update_article_citation(4, "title", "author", "journal", "2020")
        update_inproceedings_citation(5, "title", "author", "booktitle", "2020")
        update_inproceedings_citation(6, "title", "author", "booktitle", "2020")
        self.assertEqual(mock_db.session.execute.call_count, 6)
