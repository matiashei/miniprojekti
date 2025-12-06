from entities.citation_types import CitationTypes


class CitationService:
    def __init__(self, citation_repo, tag_repo, validator):
        self.citation_repo = citation_repo
        self.tag_repo = tag_repo
        self.validator = validator

    def create_citation(self, citation_type, form_data):
        if citation_type == CitationTypes.BOOK.value:
            title = form_data.get("title")
            author = form_data.get("author")
            publisher = form_data.get("publisher")
            isbn = form_data.get("isbn")
            year = form_data.get("year")

            self.validator.validate_book(title, author, publisher, isbn, year)
            citation_id = self.citation_repo.create_book_citation(
                citation_type, title, author, publisher, isbn, year
            )
        elif citation_type == CitationTypes.INPROCEEDINGS.value:
            title = form_data.get("title")
            author = form_data.get("author")
            booktitle = form_data.get("booktitle")
            year = form_data.get("year")

            self.validator.validate_inproceedings(title, author, booktitle, year)
            citation_id = self.citation_repo.create_inproceedings_citation(
                citation_type, title, author, booktitle, year
            )
        elif citation_type == CitationTypes.ARTICLE.value:
            title = form_data.get("title")
            author = form_data.get("author")
            journal = form_data.get("journal")
            year = form_data.get("year")

            self.validator.validate_article(title, author, journal, year)
            citation_id = self.citation_repo.create_article_citation(
                citation_type, title, author, journal, year
            )
        else:
            raise ValueError("Invalid citation type '{citation_type}'")

        tags = self.clean_tags(form_data.get("tags"))
        self.validator.validate_tags(tags)
        self.tag_repo.create_tags(citation_id, tags)
        return citation_id

    def update_citation(self, citation_id, citation_type, form_data):
        if citation_type == CitationTypes.BOOK.value:
            title = form_data.get("title")
            author = form_data.get("author")
            publisher = form_data.get("publisher")
            isbn = form_data.get("isbn")
            year = form_data.get("year")

            self.validator.validate_book(title, author, publisher, isbn, year)
            self.citation_repo.update_book_citation(
                citation_id, title, author, publisher, isbn, year
            )
        elif citation_type == CitationTypes.INPROCEEDINGS.value:
            title = form_data.get("title")
            author = form_data.get("author")
            booktitle = form_data.get("booktitle")
            year = form_data.get("year")

            self.validator.validate_inproceedings(title, author, booktitle, year)
            self.citation_repo.update_inproceedings_citation(
                citation_id, title, author, booktitle, year
            )
        elif citation_type == CitationTypes.ARTICLE.value:
            title = form_data.get("title")
            author = form_data.get("author")
            journal = form_data.get("journal")
            year = form_data.get("year")

            self.validator.validate_article(title, author, journal, year)
            self.citation_repo.update_article_citation(
                citation_id, title, author, journal, year
            )

        tags = self.clean_tags(form_data.get("tags"))
        self.validator.validate_tags(tags)
        self.tag_repo.update_tags(citation_id, tags)

    def delete_citation(self, form_data):
        for citation_id in form_data.getlist("citation_id"):
            self.citation_repo.delete_citation(citation_id)

    def clean_tags(self, tags_string):
        if not tags_string or tags_string.isspace():
            return []

        tags = tags_string.split(",")
        cleaned_tags = []
        for tag in tags:
            cleaned_tag = tag.strip()
            if cleaned_tag:
                cleaned_tags.append(cleaned_tag.lower())
        return list(dict.fromkeys(cleaned_tags))
