from sqlalchemy import text
from config import db, app
from entities.citation import Citation
from repositories.tags_repository import get_citation_tags

def get_citation(id):
    sql = text("""SELECT id, type, title, author, publisher, isbn,
               year, booktitle, journal FROM citations WHERE id = :id""")
    result = db.session.execute(sql, { "id": id })
    citation = result.fetchone()

    if citation:
        return Citation(
            citation_id=citation.id,
            type=citation.type,
            title=citation.title,
            author=citation.author,
            publisher=citation.publisher,
            isbn=citation.isbn,
            year=citation.year,
            booktitle=citation.booktitle,
            journal=citation.journal
        )
    else:
        return None

def get_all_citations():
    result = db.session.execute(text("SELECT * FROM citations"))
    citations = result.fetchall()

    citation_objects = []
    for citation in citations:
        tag_list = get_citation_tags(citation.id)
        citation_objects.append(
            Citation(
                citation_id=citation.id,
                type=citation.type,
                title=citation.title,
                author=citation.author,
                publisher=citation.publisher,
                isbn=citation.isbn,
                year=citation.year,
                booktitle=citation.booktitle,
                journal=citation.journal,
                tags = tag_list
            )
        )

    return citation_objects

def create_book_citation(citation_type, title, author, publisher, isbn, year):
    with app.app_context():
        sql = text("""INSERT INTO citations
            (type, title, author, publisher, isbn, year)
            VALUES (:citation_type, :title, :author, :publisher, :isbn, :year)
            RETURNING id
        """)

        result = db.session.execute(sql, { "citation_type": citation_type, "title": title, "author": author,
                                "publisher": publisher, "isbn": isbn, "year": year })
        db.session.commit()

        return result.fetchone()[0]

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
