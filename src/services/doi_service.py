import requests
from urllib.parse import quote


class DoiService:
    DOI_BASE_URL = "https://doi.org/{}"
    HEADERS = {"Accept": "application/x-bibtex; charset=utf-8"}

    @staticmethod
    def fetch_bibtex_from_doi(doi: str):
        url = DoiService.DOI_BASE_URL.format(quote(doi.strip()))

        try:
            response = requests.get(url, headers=DoiService.HEADERS, timeout=10)
            return response.text if response.ok else None
        except requests.RequestException as e:
            return None
