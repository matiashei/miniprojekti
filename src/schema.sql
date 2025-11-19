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
)
