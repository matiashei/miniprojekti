import os
from sqlalchemy import text
from config import db, app

def reset_db():
    print("Clearing contents from table tags")
    sql = text("DELETE FROM tags")
    db.session.execute(sql)
    print("Clearing contents from table citations")
    sql = text("DELETE FROM citations")
    db.session.execute(sql)
    db.session.commit()

def tables():
    sql = text(
      "SELECT table_name "
      "FROM information_schema.tables "
      "WHERE table_schema = 'public' "
      "AND table_name NOT LIKE '%_id_seq'"
    )

    result = db.session.execute(sql)
    return [row[0] for row in result.fetchall()]

def setup_db():
    tables_in_db = tables()
    if len(tables_in_db) > 0:
        print(f"Tables exist, dropping: {', '.join(tables_in_db)}")
        for table in tables_in_db:
            sql = text(f"DROP TABLE {table} CASCADE")
            db.session.execute(sql)
        db.session.commit()

    print("Creating database")

    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with open(schema_path, 'r') as f:
        schema_sql = f.read().strip()

    sql = text(schema_sql)
    db.session.execute(sql)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        setup_db()
