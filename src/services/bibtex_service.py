class BibtexService:
    def __init__(self, citation_repo):
        self.citation_repo = citation_repo

    def get_bibtex_citation(self, citation_id):
        citation = self.citation_repo.get_citation(citation_id)
        if not citation:
            return None

        if citation.type == "book":
            return self.get_book_bibtex(citation, citation_id)
        if citation.type == "inproceedings":
            return self.get_inproceedings_bibtex(citation, citation_id)
        if citation.type == "article":
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
