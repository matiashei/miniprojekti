from sqlalchemy import text
from config import db, app
from entities.citation import Citation
from repositories.tags_repository import tag_repo

class CitationRepository:
    def __init__(self):
        self.tag_repo = tag_repo

    def get_citation(self, citation_id):
        sql = text("""
            SELECT id, type, title, author, publisher, isbn, year, booktitle, journal 
            FROM citations 
            WHERE id = :id
        """)

        result = db.session.execute(sql, {"id": citation_id})
        citation = result.fetchone()

        if citation:
            tags = self.tag_repo.get_citation_tags(citation.id)

            return Citation(
                citation_id=citation.id,
                citation_type=citation.type,
                title=citation.title,
                author=citation.author,
                publisher=citation.publisher,
                isbn=citation.isbn,
                year=citation.year,
                booktitle=citation.booktitle,
                journal=citation.journal,
                tags=tags
            )
        else:
            return None

    def get_all_citations(self):
        result = db.session.execute(text("SELECT * FROM citations"))
        citations = result.fetchall()

        citation_objects = []
        for citation in citations:
            tag_list = self.tag_repo.get_citation_tags(citation.id)
            citation_objects.append(
                Citation(
                    citation_id=citation.id,
                    citation_type=citation.type,
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

    def create_book_citation(self, citation_type, title, author, publisher, isbn, year):
        with app.app_context():
            sql = text("""
                INSERT INTO citations (type, title, author, publisher, isbn, year)
                VALUES (:citation_type, :title, :author, :publisher, :isbn, :year)
                RETURNING id
            """)

            result = db.session.execute(sql, {"citation_type": citation_type, "title": title,
                                            "author": author, "publisher": publisher, "isbn": isbn,
                                            "year": year})
            db.session.commit()
            return result.fetchone()[0]

    def create_inproceedings_citation(self, citation_type, title, author, booktitle, year):
        with app.app_context():
            sql = text("""
                INSERT INTO citations (type, title, author, booktitle, year)
                VALUES (:citation_type, :title, :author, :booktitle, :year)
                RETURNING id
            """)

            result = db.session.execute(sql, {"citation_type": citation_type, "title": title,
                                            "author": author, "booktitle": booktitle, "year": year})
            db.session.commit()
            return result.fetchone()[0]

    def create_article_citation(self, citation_type, title, author, journal, year):
        with app.app_context():
            sql = text("""
                INSERT INTO citations (type, title, author, journal, year)
                VALUES (:citation_type, :title, :author, :journal, :year)
                RETURNING id
            """)

            result = db.session.execute(sql, {"citation_type": citation_type, "title": title,
                                            "author": author, "journal": journal, "year": year})
            db.session.commit()
            return result.fetchone()[0]

    def delete_citation(self, citation_id):
        with app.app_context():
            sql = text("DELETE FROM citations WHERE id = :id")
            db.session.execute(sql, {"id": citation_id})
            db.session.commit()

    def update_book_citation(self, citation_id, title, author, publisher, isbn, year):
        with app.app_context():
            sql = text("""
                UPDATE citations
                SET title = :title,
                    author = :author,
                    publisher = :publisher,
                    isbn = :isbn,
                    year = :year
                WHERE id = :id
            """)
            db.session.execute(sql, {"id": citation_id, "title": title, "author": author,
                                    "publisher": publisher, "isbn": isbn, "year": year})
            db.session.commit()

    def update_inproceedings_citation(self, citation_id, title, author, booktitle, year):
        with app.app_context():
            sql = text("""
                UPDATE citations
                SET title = :title,
                    author = :author,
                    booktitle = :booktitle,
                    year = :year
                WHERE id = :id
            """)
            db.session.execute(sql, {"id": citation_id, "title": title, "author": author,
                                    "booktitle": booktitle, "year": year})
            db.session.commit()

    def update_article_citation(self, citation_id, title, author, journal, year):
        with app.app_context():
            sql = text("""
                UPDATE citations
                SET title = :title,
                    author = :author,
                    journal = :journal,
                    year = :year
                WHERE id = :id
            """)
            db.session.execute(sql, {"id": citation_id, "title": title, "author": author,
                                    "journal": journal, "year": year})
            db.session.commit()

    def get_bibtex_citation(self, citation_id):
        citation = self.get_citation(citation_id)
        if not citation:
            return None

        if citation.type == "book":
            return self.get_book_bibtex(citation, citation_id)
        if citation.type == "inproceedings":
            return self.get_inproceedings_bibtex(citation, citation_id)
        if citation.type == "article":
            return self.get_article_bibtex(citation, citation_id)
        return None

    def get_book_bibtex(self, citation, citation_id):
        bibtex = f"@book{{book{citation_id},\n"
        bibtex += f"    author = {{{citation.author}}},\n"
        bibtex += f"    title = {{{citation.title}}},\n"
        bibtex += f"    year = {{{citation.year}}},\n"
        bibtex += f"    publisher = {{{citation.publisher}}},\n"
        bibtex += f"    isbn = {{{citation.isbn}}}\n"
        bibtex += "}"
        return bibtex

    def get_inproceedings_bibtex(self, citation, citation_id):
        bibtex = f"@inproceedings{{inproceedings{citation_id},\n"
        bibtex += f"    author = {{{citation.author}}},\n"
        bibtex += f"    title = {{{citation.title}}},\n"
        bibtex += f"    year = {{{citation.year}}},\n"
        bibtex += f"    booktitle = {{{citation.booktitle}}}\n"
        bibtex += "}"
        return bibtex

    def get_article_bibtex(self, citation, citation_id):
        bibtex = f"@article{{article{citation_id},\n"
        bibtex += f"    author = {{{citation.author}}},\n"
        bibtex += f"    title = {{{citation.title}}},\n"
        bibtex += f"    journal = {{{citation.journal}}},\n"
        bibtex += f"    year = {{{citation.year}}}\n"
        bibtex += "}"
        return bibtex


citation_repo = CitationRepository()
