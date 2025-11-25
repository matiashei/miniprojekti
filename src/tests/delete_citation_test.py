import unittest

from unittest.mock import patch
from repositories.citation_repository import delete_citation

class TestDeleteCitation(unittest.TestCase):
    def setUp(self):
        self.citation_id = [1, 2]

    # Using patch to mock the database so we don't touch the real db
    @patch("repositories.citation_repository.db")
    def test_delete_one_citation(self, mock_db):
        delete_citation(self.citation_id[0])
        mock_db.session.execute.assert_called_once()

    @patch("repositories.citation_repository.db")
    def test_delete_nonexistent_citation_fails(self, mock_db):
        mock_db.session.execute.side_effect = Exception()
        with self.assertRaises(Exception):
            delete_citation(999)

    @patch("repositories.citation_repository.db")
    def test_delete_several_citations(self, mock_db):
        delete_citation(self.citation_id[0])
        delete_citation(self.citation_id[1])
        self.assertEqual(mock_db.session.execute.call_count, 2)
