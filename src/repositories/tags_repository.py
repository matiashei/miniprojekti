from unittest import result
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from config import db, app

class TagRepository:
    def __init__(self):
        pass

    def create_tags(self, citation_id: int, tags: list):
        with app.app_context():
            for tag in tags:
                try:
                    sql = text("""
                        INSERT INTO tags (citation_id, tag)
                        VALUES (:citation_id, :tag)
                    """)

                    db.session.execute(sql, {"citation_id": citation_id, "tag": tag})
                except IntegrityError:
                    db.session.rollback()
                    continue
            db.session.commit()

    def update_tags(self, citation_id: int, tags: list):
        with app.app_context():
            sql = text("DELETE FROM tags WHERE citation_id = :citation_id")
            db.session.execute(sql, {"citation_id": citation_id})

            sql = text("INSERT INTO tags (citation_id, tag) VALUES (:citation_id, :tag)")
            for tag in tags:
                db.session.execute(sql, {"citation_id": citation_id, "tag": tag})

            db.session.commit()

    def get_citation_tags(self, citation_id):
        with app.app_context():
            sql = text("""
                SELECT tag FROM tags
                WHERE citation_id = :citation_id
            """)

            result = db.session.execute(sql, {"citation_id": citation_id}).fetchall()
            return [row.tag for row in result] if result else []

    def get_all_tags(self):
        sql = text("SELECT DISTINCT tag FROM tags ORDER BY tag")
        result = db.session.execute(sql)
        return [row[0] for row in result.fetchall()]

    def search_citations_by_tag(self, tags):
        with app.app_context():
            placeholders = ', '.join([':tag{}'.format(i) for i in range(len(tags))])
            sql = text(f"""
                SELECT citation_id FROM tags
                WHERE tag IN ({placeholders})
            """)

            result = db.session.execute(sql, {f'tag{i}': tag for i, tag in enumerate(tags)}).fetchall()

        citation_ids = []
        for row in result:
            citation_ids.append(row.citation_id)

        return citation_ids