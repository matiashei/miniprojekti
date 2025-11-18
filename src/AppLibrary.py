import requests
from repositories.citation_repository import create_book_citation

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"

    def reset_database(self):
        requests.post(f"{self._base_url}/reset_db")

    # disable pylint for now as this method will likely change in the future
    # pylint: disable=too-many-arguments
    def create_book_citation(self, title, author, publisher, isbn, year):
        create_book_citation(title, author, publisher, isbn, year)
