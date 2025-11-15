from config import db
from sqlalchemy import text

from entities.citation import Citation

def get_citations():
    result = db.session.execute(text("SELECT id, content FROM citations"))
    citations = result.fetchall()
    return [Citation(citation[0], citation[1]) for citation in citations]

def create_citation(content):
    sql = text("INSERT INTO citations (content) VALUES (:content)")
    db.session.execute(sql, { "content": content })
    db.session.commit()
