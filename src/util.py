class UserInputError(Exception):
    pass

def validate_book(title, author, publisher, isbn, year):
    if not title or title.isspace() or len(title) > 75:
        raise UserInputError("Title cannot be empty and the lenght must be less than 75 characters")

    if author.isspace() or len(author) > 75:
        raise UserInputError("Author length must be less than 75 characters")

    if publisher.isspace() or len(publisher) > 50:
        raise UserInputError("Publisher length must be less than 50 characters")

    if isbn.isspace() or len(isbn) > 20:
        raise UserInputError("ISBN lenght must be less than 20 characters")

    if year.isspace() or int(year) < 0 or int(year) > 2025:
        raise UserInputError("Invalid year")

def validate_inproceedings(title, author, booktitle, year):
    if not title or title.isspace() or len(title) > 75:
        raise UserInputError("Title length must be less than 75 characters")

    if author.isspace() or len(author) > 75:
        raise UserInputError("Author length must be less than 75 characters")

    if booktitle.isspace() or len(booktitle) > 75:
        raise UserInputError("Booktitle length must be less than 75 characters")

    if year.isspace() or int(year) < 0 or int(year) > 2025:
        raise UserInputError("Invalid year")

def validate_article(title, author, journal, year):
    if not title or title.isspace() or len(title) > 75:
        raise UserInputError("Title length must be less than 75 characters")

    if author.isspace() or len(author) > 75:
        raise UserInputError("Author length must be less than 75 characters")

    if journal.isspace() or len(journal) > 75:
        raise UserInputError("Journal length must be less than 75 characters")

    if year.isspace() or int(year) < 0 or int(year) > 2025:
        raise UserInputError("Invalid year")
