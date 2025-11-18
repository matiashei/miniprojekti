from sqlalchemy import text
from config import db, app

from entities.citation import Citation

def get_citations():
    result = db.session.execute(text("SELECT id, content FROM citations"))
    citations = result.fetchall()
    return [Citation(citation[0], citation[1]) for citation in citations]

def create_citation(content):
    sql = text("INSERT INTO citations (content) VALUES (:content)")
    db.session.execute(sql, { "content": content })
    db.session.commit()

def create_book_citation(title, author, publisher, isbn, year):
    with app.app_context():
        sql = text("INSERT INTO citations (title, author, publisher, isbn, year) " \
        "VALUES (:title, :author, :publisher, :isbn, :year)")

        db.session.execute(sql, { "title": title, "author": author, "publisher": publisher,
                                "isbn": isbn, "year": year })
        db.session.commit()

# Temporary function to get book citations for front page listing
def get_book_citations():
    result = db.session.execute(text("SELECT title, author, publisher, isbn, year " \
    "FROM citations"))
    book_citations = result.fetchall()
    return book_citations
