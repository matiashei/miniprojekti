CREATE TABLE citations (
  id SERIAL PRIMARY KEY,
  type TEXT,
  title TEXT,
  author TEXT,
  publisher TEXT,
  booktitle TEXT,
  journal TEXT,
  isbn TEXT,
  year INT
);

CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  citation_id INTEGER REFERENCES citations(id) ON DELETE CASCADE,
  tag TEXT,
  UNIQUE(citation_id, tag)
);
