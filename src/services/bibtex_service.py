from entities.citation_types import CitationTypes
import re


class BibtexService:
    def __init__(self, citation_repo):
        self.citation_repo = citation_repo

    def get_bibtex_citation(self, citation_id):
        citation = self.citation_repo.get_citation(citation_id)
        if not citation:
            return None

        if citation.type == CitationTypes.BOOK.value:
            return self.get_book_bibtex(citation, citation_id)
        if citation.type == CitationTypes.INPROCEEDINGS.value:
            return self.get_inproceedings_bibtex(citation, citation_id)
        if citation.type == CitationTypes.ARTICLE.value:
            return self.get_article_bibtex(citation, citation_id)
        return None

    def get_book_bibtex(self, citation, citation_id):
        bibtex = f"@book{{book{citation_id},\n"
        bibtex += f"    author = {{{citation.author}}},\n"
        bibtex += f"    title = {{{citation.title}}},\n"
        bibtex += f"    year = {{{citation.year}}},\n"
        bibtex += f"    publisher = {{{citation.publisher}}},\n"
        bibtex += f"    isbn = {{{citation.isbn}}}\n"
        bibtex += "}"
        return bibtex

    def get_inproceedings_bibtex(self, citation, citation_id):
        bibtex = f"@inproceedings{{inproceedings{citation_id},\n"
        bibtex += f"    author = {{{citation.author}}},\n"
        bibtex += f"    title = {{{citation.title}}},\n"
        bibtex += f"    year = {{{citation.year}}},\n"
        bibtex += f"    booktitle = {{{citation.booktitle}}}\n"
        bibtex += "}"
        return bibtex

    def get_article_bibtex(self, citation, citation_id):
        bibtex = f"@article{{article{citation_id},\n"
        bibtex += f"    author = {{{citation.author}}},\n"
        bibtex += f"    title = {{{citation.title}}},\n"
        bibtex += f"    journal = {{{citation.journal}}},\n"
        bibtex += f"    year = {{{citation.year}}}\n"
        bibtex += "}"
        return bibtex

    def parse_bibtex_string(self, bibtex: str):
        header_match = re.search(r'@\s*([^{\s]+)\s*{\s*([^,]+),',
                        bibtex, re.IGNORECASE)

        type = header_match.group(1).lower()
        field_pattern = re.compile(r'(\w+)\s*=\s*(\{([^{}]*)\}|"([^"]*)")\s*,?',
                        re.IGNORECASE)
        fields_raw = {}

        for match in field_pattern.finditer(bibtex):
            key = match.group(1).lower()

            if match.group(3):
                value = match.group(3)
            else:
                value = match.group(4)

            fields_raw[key] = value.strip()

        if type == "book":
            citation_type = CitationTypes.BOOK.value
            mapped_fields = {
                "title": fields_raw.get("title", ""),
                "author": fields_raw.get("author", ""),
                "publisher": fields_raw.get("publisher", ""),
                "isbn": fields_raw.get("isbn", ""),
                "year": fields_raw.get("year", ""),
            }

        elif type == "article":
            citation_type = CitationTypes.ARTICLE.value
            mapped_fields = {
                "title": fields_raw.get("title", ""),
                "author": fields_raw.get("author", ""),
                "journal": fields_raw.get("journal", ""),
                "year": fields_raw.get("year", ""),
            }

        elif type in ("inproceedings", "conference", "incollection"):
            citation_type = CitationTypes.INPROCEEDINGS.value
            mapped_fields = {
                "title": fields_raw.get("title", ""),
                "author": fields_raw.get("author", ""),
                "booktitle": fields_raw.get("booktitle", ""),
                "year": fields_raw.get("year", ""),
            }

        return {
            "type": citation_type,
            "fields": mapped_fields
        }
