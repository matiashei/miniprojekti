from sqlalchemy import text
from config import db, app

def create_book_citation(citation_type, title, author, publisher, isbn, year):
    with app.app_context():
        sql = text("""INSERT INTO citations
            (type, title, author, publisher, isbn, year)
            VALUES (:citation_type, :title, :author, :publisher, :isbn, :year)
        """)

        db.session.execute(sql, { "citation_type": citation_type, "title": title, "author": author,
                                "publisher": publisher, "isbn": isbn, "year": year })
        db.session.commit()

def create_inproceedings_citation(citation_type, title, author, booktitle, year):
    with app.app_context():
        citation_type = "inproceedings"
        sql = text("""INSERT INTO citations
        (type, title, author, booktitle, year)
        VALUES (:citation_type, :title, :author, :booktitle, :year)
        """)

        db.session.execute(sql, { "citation_type": citation_type, "title": title, "author": author,
                                "booktitle": booktitle, "year": year })
        db.session.commit()

def create_article_citation(citation_type, title, author, journal, year):
    with app.app_context():
        sql = text("""INSERT INTO citations
            (type, title, author, journal, year)
            VALUES (:citation_type, :title, :author, :journal, :year)
        """)

        db.session.execute(sql, { "citation_type": citation_type, "title": title, "author": author,
                                "journal": journal, "year": year })
        db.session.commit()

def delete_citation(citation_id):
    with app.app_context():
        sql = text("DELETE FROM citations WHERE id = :id")
        db.session.execute(sql, {"id": citation_id})
        db.session.commit()

# Temporary function to get all citations for front page listing
def get_book_citations():
    result = db.session.execute(text("SELECT * " \
    "FROM citations"))
    book_citations = result.fetchall()
    return book_citations
