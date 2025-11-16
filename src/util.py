class UserInputError(Exception):
    pass

def validate_citation(content):
    if len(content) < 5:
        raise UserInputError("citation content length must be greater than 4")

    if len(content) > 100:
        raise UserInputError("citation content length must be smaller than 100")
    
def validate_book(title, author, publisher, isbn, year):
    if title.isspace() or len(title) > 75:
        raise UserInputError("Title length must be les thean 75")
    
    if author.isspace() or len(author) > 75:
        raise UserInputError("Author length must be less than 75")

    if publisher.isspace() or len(publisher) > 50:
        raise UserInputError("Publisher length must be less than 50")

    if isbn.isspace() or len(isbn) > 20:
        raise UserInputError("Isbn lenght must be less than 20")

    if year.isspace() or int(year) < 0 or int(year) > 2025:
        raise UserInputError("Invalid year")
    
    
