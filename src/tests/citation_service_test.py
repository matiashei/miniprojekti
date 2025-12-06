import unittest
from services.citation_service import CitationService


class TestCleanTags(unittest.TestCase):
    def setUp(self):
        self.citations = CitationService()

    def test_clean_tags(self):
        self.assertEqual(self.citations.clean_tags(" tag ,  tag2 ,tag3 "), ["tag", "tag2", "tag3"])
