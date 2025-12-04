from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.citation_repository import CitationRepository
from repositories.tags_repository import (
    create_tags,
    get_citation_tags,
    update_tags
)

from config import app, test_env
from util import (
    validate_book,
    validate_inproceedings,
    validate_article,
    clean_tags,
    validate_tags
)

citation_repo = CitationRepository()

@app.route("/")
def index():
    citations = citation_repo.get_all_citations()
    return render_template("index.html", citations=citations)

@app.route("/new_citation")
def new():
    return render_template("new_citation.html")

@app.route("/create_book_citation", methods=["POST"])
def citation_creation_book():
    title = request.form.get("title")
    author = request.form.get("author")
    publisher = request.form.get("publisher")
    isbn = request.form.get("isbn")
    year = request.form.get("year")
    citation_type = "book"
    tags = clean_tags(request.form.get("tags"))

    try:
        validate_book(title, author, publisher, isbn, year)
        citation_id = citation_repo.create_book_citation(
            citation_type, title, author, publisher, isbn, year
        )
        validate_tags(tags)
        create_tags(citation_id, tags)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_citation")

@app.route("/create_inproceedings_citation", methods=["POST"])
def citation_creation_inproceedings():
    title = request.form.get("title")
    author = request.form.get("author")
    booktitle = request.form.get("booktitle")
    year = request.form.get("year")
    citation_type = "inproceedings"
    tags = clean_tags(request.form.get("tags"))

    try:
        validate_inproceedings(title, author, booktitle, year)
        citation_id = citation_repo.create_inproceedings_citation(
            citation_type, title, author, booktitle, year
        )
        validate_tags(tags)
        create_tags(citation_id, tags)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_citation")

@app.route("/create_article_citation", methods=["POST"])
def citation_creation_article():
    title = request.form.get("title")
    author = request.form.get("author")
    journal = request.form.get("journal")
    year = request.form.get("year")
    citation_type = "article"
    tags = clean_tags(request.form.get("tags"))

    try:
        validate_article(title, author, journal, year)
        citation_id = citation_repo.create_article_citation(
            citation_type, title, author, journal, year
        )
        validate_tags(tags)
        create_tags(citation_id, tags)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_citation")

@app.route("/edit_citation/<int:id>")
def edit_citation(id):
    tags = get_citation_tags(id)
    if tags is None:
        tags = []

    citation = citation_repo.get_citation(id, tags)
    if citation is None:
        return redirect("/")

    return render_template("edit_citation.html", citation=citation)

@app.route("/edit_book_citation/<int:id>", methods=["POST"])
def citation_edition_book(id):
    title = request.form.get("title")
    author = request.form.get("author")
    publisher = request.form.get("publisher")
    isbn = request.form.get("isbn")
    year = request.form.get("year")
    tags = clean_tags(request.form.get("tags"))

    try:
        validate_book(title, author, publisher, isbn, year)
        citation_repo.update_book_citation(id, title, author, publisher, isbn, year)
        validate_tags(tags)
        update_tags(id, tags)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect(f"/edit_citation/{id}")

@app.route("/edit_inproceedings_citation/<int:id>", methods=["POST"])
def citation_edition_inproceedings(id):
    title = request.form.get("title")
    author = request.form.get("author")
    booktitle = request.form.get("booktitle")
    year = request.form.get("year")
    tags = clean_tags(request.form.get("tags"))

    try:
        validate_inproceedings(title, author, booktitle, year)
        citation_repo.update_inproceedings_citation(id, title, author, booktitle, year)
        validate_tags(tags)
        update_tags(id, tags)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect(f"/edit_citation/{id}")

@app.route("/edit_article_citation/<int:id>", methods=["POST"])
def citation_edition_article(id):
    title = request.form.get("title")
    author = request.form.get("author")
    journal = request.form.get("journal")
    year = request.form.get("year")
    tags = clean_tags(request.form.get("tags"))

    try:
        validate_article(title, author, journal, year)
        citation_repo.update_article_citation(id, title, author, journal, year)
        validate_tags(tags)
        update_tags(id, tags)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect(f"/edit_citation/{id}")

@app.route("/delete_citations", methods=["POST"])
def delete_citations():
    for citation_id in request.form.getlist("citation_id"):
        try:
            citation_repo.delete_citation(citation_id)
        except Exception as error:
            flash(str(error))
            return redirect("/")
    return redirect("/")

@app.route("/bibtex", methods=["GET","POST"])
def get_bibtex():
    bibtex_results = []
    for citation in citation_repo.get_all_citations():
        bibtex = citation_repo.get_bibtex_citation(citation.id)
        bibtex_results.append(bibtex)

    return render_template("bibtex.html", bibtex_results=bibtex_results)


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db", methods=["POST"])
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
