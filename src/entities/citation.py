class Citation:
    def __init__(self, citation_id, type, title, author, publisher, isbn, year, booktitle, journal):
        self.id = citation_id
        self.type = type
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.year = year
        self.booktitle = booktitle
        self.journal = journal
