import requests
from repositories.citation_repository import CitationRepository
from repositories.tags_repository import TagRepository

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"
        self.tag_repo = TagRepository()
        self.citation_repo = CitationRepository(self.tag_repo)

    def reset_database(self):
        requests.post(f"{self._base_url}/reset_db")

    def create_book_citation(self, title, author, publisher, isbn, year, tags=None):
        citation_id = self.citation_repo.create_book_citation(
            "book", title, author, publisher, isbn, year
        )
        if tags:
            self.tag_repo.create_tags(citation_id, tags)

    def create_inproceedings_citation(self, title, author, booktitle, year, tags=None):
        citation_id = self.citation_repo.create_inproceedings_citation(
            "inproceedings", title, author, booktitle, year
        )
        if tags:
            self.tag_repo.create_tags(citation_id, tags)

    def create_article_citation(self, title, author, journal, year, tags=None):
        citation_id = self.citation_repo.create_article_citation(
            "article", title, author, journal, year
        )
        if tags:
            self.tag_repo.create_tags(citation_id, tags)
