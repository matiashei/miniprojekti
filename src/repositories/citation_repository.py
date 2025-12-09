from sqlalchemy import text
from config import db, app
from entities.citation import Citation

class CitationRepository:
    def __init__(self, tag_repo):
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

    def get_citations_by_tag(self, tags, match_all=False):
        if not tags:
            return []

        if match_all:
            return self.get_citations_with_all_tags(tags)
        else:
            return self.get_citations_with_any_tag(tags)

    def get_citations_with_all_tags(self, tags):
        if not tags:
            return []

        placeholders = ",".join(f"'{tag}'" for tag in tags)
        tag_count = len(tags)

        sql = text(f"""
                SELECT c.*
                FROM citations c
                WHERE c.id IN (
                    -- Viittaukset, joilla on kaikki haetut tagit (Kuten nykyinen match_all)
                    SELECT citation_id
                    FROM tags
                    WHERE tag IN ({placeholders})
                    GROUP BY citation_id
                    HAVING COUNT(DISTINCT tag) = :tag_count
                )
            """)

        result = db.session.execute(sql, {"tag_count": tag_count})
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
                    tags=tag_list if tag_list else []
                )
            )

        return citation_objects

    def get_citations_with_any_tag(self, tags):
        if not tags:
            return []

        placeholders = ",".join(f"'{tag}'" for tag in tags)
        sql = text(f"""
            SELECT DISTINCT c.id, c.type, c.title, c.author, c.publisher, c.isbn,
                c.year, c.booktitle, c.journal
            FROM citations c
            JOIN tags t ON c.id = t.citation_id
            WHERE t.tag IN ({placeholders})
            ORDER BY c.id
        """)

        result = db.session.execute(sql)
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
                    tags=tag_list if tag_list else []
                )
            )

        return citation_objects

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
