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


tag_repo = TagRepository()
