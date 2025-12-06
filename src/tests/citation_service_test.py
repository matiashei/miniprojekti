import unittest
from unittest.mock import Mock
from services.citation_service import CitationService


class TestCleanTags(unittest.TestCase):
    def setUp(self):
        self.citation_repo = Mock()
        self.tag_repo = Mock()
        self.validator = Mock()
        self.citations = CitationService(self.citation_repo, self.tag_repo, self.validator)

    def test_clean_tags(self):
        self.assertEqual(self.citations.clean_tags(" tag ,  tag2 ,tag3 "), ["tag", "tag2", "tag3"])
