import unittest
from unittest.mock import patch, ANY

from repositories.citation_repository import CitationRepository
from repositories.tags_repository import TagRepository

class TestCreateCitation(unittest.TestCase):
    def setUp(self):
        self.book_citation = ("book", "Title", "Author", "Publisher", "1234", "2023")
        self.inproceedings_citation = ("inproceedings", "Title", "Author", "Booktitle", "2023")
        self.article_citation = ("article", "Title", "Author", "Journal", "2023")
        self.tag_repo = TagRepository()
        self.citation_repo = CitationRepository(self.tag_repo)

    @patch("repositories.citation_repository.db")
    def test_create_valid_book_citation(self, mock_db):
        self.citation_repo.create_book_citation(*self.book_citation)

        mock_db.session.execute.assert_called_once_with(ANY, {
            "citation_type": self.book_citation[0],
            "title": self.book_citation[1],
            "author": self.book_citation[2],
            "publisher": self.book_citation[3],
            "isbn": self.book_citation[4],
            "year": self.book_citation[5]
            }
        )
        mock_db.session.commit.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_create_valid_inproceedings_citation(self, mock_db):
        self.citation_repo.create_inproceedings_citation(*self.inproceedings_citation)

        mock_db.session.execute.assert_called_once_with(ANY, {
            "citation_type": self.inproceedings_citation[0],
            "title": self.inproceedings_citation[1],
            "author": self.inproceedings_citation[2],
            "booktitle": self.inproceedings_citation[3],
            "year": self.inproceedings_citation[4]
            }
        )
        mock_db.session.commit.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_create_valid_article_citation(self, mock_db):
        self.citation_repo.create_article_citation(*self.article_citation)

        mock_db.session.execute.assert_called_once_with(ANY, {
            "citation_type": self.article_citation[0],
            "title": self.article_citation[1],
            "author": self.article_citation[2],
            "journal": self.article_citation[3],
            "year": self.article_citation[4]
            }
        )
        mock_db.session.commit.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_create_consecutive_citations(self, mock_db):
        self.citation_repo.create_book_citation(*self.book_citation)
        self.citation_repo.create_article_citation(*self.article_citation)
        self.citation_repo.create_inproceedings_citation(*self.inproceedings_citation)

        self.assertEqual(mock_db.session.execute.call_count, 3)
