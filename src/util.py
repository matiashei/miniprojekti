class UserInputError(Exception):
    pass

def validate_book(title, author, publisher, isbn, year):
    if not title or title.isspace() or len(title) > 75:
        raise UserInputError(
            "Title cannot be empty and the length must be less than 75 characters"
            )

    if not author or author.isspace() or len(author) > 75:
        raise UserInputError(
            "Author cannot be empty and the length must be less than 75 characters"
            )

    if not publisher or publisher.isspace() or len(publisher) > 50:
        raise UserInputError(
            "Publisher cannot be empty and the length must be less than 50 characters"
            )

    if not isbn or isbn.isspace() or len(isbn) > 20:
        raise UserInputError(
            "ISBN cannot be empty and the length must be less than 20 characters"
            )

    if not year or year.isspace() or int(year) < 0 or int(year) > 2025:
        raise UserInputError("Invalid year")

def validate_inproceedings(title, author, booktitle, year):
    if not title or title.isspace() or len(title) > 75:
        raise UserInputError(
            "Title cannot be empty and the length must be less than 75 characters"
            )

    if not author or author.isspace() or len(author) > 75:
        raise UserInputError(
            "Author cannot be empty and the length must be less than 75 characters"
            )

    if not booktitle or booktitle.isspace() or len(booktitle) > 75:
        raise UserInputError(
            "Booktitle cannot be empty and the length must be less than 75 characters"
            )

    if not year or year.isspace() or int(year) < 0 or int(year) > 2025:
        raise UserInputError("Invalid year")

def validate_article(title, author, journal, year):
    if not title or title.isspace() or len(title) > 75:
        raise UserInputError(
            "Title cannot be empty and the length must be less than 75 characters"
            )

    if not author or author.isspace() or len(author) > 75:
        raise UserInputError(
            "Author cannot be empty and the length must be less than 75 characters"
            )

    if not journal or journal.isspace() or len(journal) > 75:
        raise UserInputError(
            "Journal cannot be empty and the length must be less than 75 characters"
            )

    if not year or year.isspace() or int(year) < 0 or int(year) > 2025:
        raise UserInputError("Invalid year")
