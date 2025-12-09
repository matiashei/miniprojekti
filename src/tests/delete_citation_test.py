import unittest
from unittest.mock import Mock, patch
from werkzeug.datastructures import MultiDict
from repositories.citation_repository import CitationRepository
from services.citation_service import CitationService

class TestDeleteCitation(unittest.TestCase):
    def setUp(self):
        self.citation_repo = CitationRepository(Mock())
        self.citation_service = CitationService(self.citation_repo, Mock(), Mock())

    # Using patch to mock the database so we don't touch the real db
    @patch("repositories.citation_repository.db")
    def test_delete_one_citation(self, mock_db):
        self.citation_service.delete_citation(MultiDict({"citation_id": ["1"]}))
        mock_db.session.execute.assert_called_once()
        mock_db.session.commit.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_delete_nonexistent_citation_fails(self, mock_db):
        mock_db.session.execute.side_effect = Exception()
        with self.assertRaises(Exception):
            self.citation_service.delete_citation(MultiDict({"citation_id": ["999"]}))

    @patch("repositories.citation_repository.db")
    def test_delete_several_citations(self, mock_db):
        self.citation_service.delete_citation(MultiDict({"citation_id": ["1", "2"]}))
        self.assertEqual(mock_db.session.execute.call_count, 2)
        self.assertEqual(mock_db.session.commit.call_count, 2)
