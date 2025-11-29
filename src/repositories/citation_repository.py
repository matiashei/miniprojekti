from sqlalchemy import text
from config import db, app
from entities.citation import Citation

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
                journal=citation.journal
            )
        )

    return citation_objects

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

def get_bibtex_citation(citation_id):
    citation = get_citation(citation_id)
    if not citation:
        return None

    if citation.type == "book":
        return get_book_bibtex(citation, citation_id)
    if citation.type == "inproceedings":
        return get_inproceedings_bibtex(citation, citation_id)
    if citation.type == "article":
        return get_article_bibtex(citation, citation_id)
    return None

def get_book_bibtex(citation, citation_id):
    bibtex = f"@book{{book{citation_id},\n"
    bibtex += f"    author = {{{citation.author}}},\n"
    bibtex += f"    title = {{{citation.title}}},\n"
    bibtex += f"    year = {{{citation.year}}},\n"
    bibtex += f"    publisher = {{{citation.publisher}}},\n"
    bibtex += f"    isbn = {{{citation.isbn}}}\n"
    bibtex += "}"
    return bibtex

def get_inproceedings_bibtex(citation, citation_id):
    bibtex = f"@inproceedings{{inproceedings{citation_id},\n"
    bibtex += f"    author = {{{citation.author}}},\n"
    bibtex += f"    title = {{{citation.title}}},\n"
    bibtex += f"    year = {{{citation.year}}},\n"
    bibtex += f"    booktitle = {{{citation.booktitle}}}\n"
    bibtex += "}"
    return bibtex

def get_article_bibtex(citation, citation_id):
    bibtex = f"@article{{article{citation_id},\n"
    bibtex += f"    author = {{{citation.author}}},\n"
    bibtex += f"    title = {{{citation.title}}},\n"
    bibtex += f"    journal = {{{citation.journal}}},\n"
    bibtex += f"    year = {{{citation.year}}}\n"
    bibtex += "}"
    return bibtex
