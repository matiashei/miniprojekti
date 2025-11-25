from sqlalchemy import text
from config import db, app


def get_citations():
    result = db.session.execute(text("SELECT id, title FROM citations"))
    citations = result.fetchall()
    return [Citation(citation[0], citation[1]) for citation in citations]

def get_citation(id):
    sql = text("SELECT id, type, title, author, publisher, isbn, year, booktitle, journal FROM citations WHERE id = :id")
    result = db.session.execute(sql, { "id": id })
    return result.fetchone() if result else None

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

def update_book_citation(id, title, author, publisher, isbn, year):
    with app.app_context():
        sql = text("""UPDATE citations
            SET title = :title,
                author = :author,
                publisher = :publisher,
                isbn = :isbn,
                year = :year
            WHERE id = :id
        """)
        db.session.execute(sql, { "id": id, "title": title, "author": author, "publisher": publisher,
                                "isbn": isbn, "year": year })
        db.session.commit()

def update_inproceedings_citation(id, title, author, booktitle, year):
    with app.app_context():
        sql = text("""UPDATE citations
            SET title = :title,
                author = :author,
                booktitle = :booktitle,
                year = :year
            WHERE id = :id
        """)
        db.session.execute(sql, { "id": id, "title": title, "author": author, "booktitle": booktitle,
                                "year": year })
        db.session.commit()

def update_article_citation(id, title, author, journal, year):
    with app.app_context():
        sql = text("""UPDATE citations
            SET title = :title,
                author = :author,
                journal = :journal,
                year = :year
            WHERE id = :id
        """)
        db.session.execute(sql, { "id": id, "title": title, "author": author, "journal": journal,
                                "year": year })
        db.session.commit()

# Temporary function to get book citations for front page listing
def get_book_citations():
    result = db.session.execute(text("SELECT id, title, author, publisher, isbn, year " \
    "FROM citations"))
    book_citations = result.fetchall()
    return book_citations
