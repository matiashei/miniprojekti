from sqlalchemy import text
from config import db, app
from entities.citation import Citation

def create_tags(citation_id: int, tags: list):
    with app.app_context():
        for tag in tags:
            sql = text("""INSERT INTO tags
                (citation_id, tag)
                VALUES (:citation_id, :tag)
            """)

            db.session.execute(sql, { "citation_id": citation_id, "tag": tag })

        db.session.commit()

def get_citation_tags(citation_id):
    with app.app_context():
        sql = text("""SELECT tag FROM tags
        WHERE citation_id = :citation_id
        """)

        result = db.session.execute(sql, { "citation_id": citation_id }).fetchall()
        return result if result else None
