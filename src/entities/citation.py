class Citation:
    def __init__(self, citation_id, citation_type, title, author, publisher, isbn, year, booktitle, journal, tags=[]):
        self.id = citation_id
        self.type = citation_type
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.year = year
        self.booktitle = booktitle
        self.journal = journal
        self.tags = tags
