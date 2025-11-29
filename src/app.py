from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.citation_repository import (
    get_all_citations,
    create_book_citation,
    create_inproceedings_citation,
    create_article_citation,
    delete_citation,
    update_book_citation,
    update_inproceedings_citation,
    update_article_citation,
    get_citation,
    get_bibtex_citation
)

from config import app, test_env
from util import validate_book, validate_inproceedings, validate_article


@app.route("/")
def index():
    # temporary function to fetch all citations
    book_citations = get_all_citations()
    return render_template("index.html", book_citations=book_citations)


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

    try:
        validate_book(title, author, publisher, isbn, year)
        create_book_citation(citation_type, title, author, publisher, isbn, year)
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

    try:
        validate_inproceedings(title, author, booktitle, year)
        create_inproceedings_citation(citation_type, title, author, booktitle, year)
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

    try:
        validate_article(title, author, journal, year)
        create_article_citation(citation_type, title, author, journal, year)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_citation")

@app.route("/edit_citation/<int:id>")
def edit_citation(id):
    citation = get_citation(id)
    print("Editing citation:", citation)
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

    try:
        validate_book(title, author, publisher, isbn, year)
        update_book_citation(id, title, author, publisher, isbn, year)
        print("Book citation updated successfully.")
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect(f"/edit_citation/{id}")

@app.route("/edit_inproceedings_citation/<int:id>", methods=["POST"])
def citation_edition_inproceedings(id):
    title = request.form.get("title")
    author = request.form.get("author")
    booktitle = request.form.get("booktitle")
    year = request.form.get("year")

    try:
        validate_inproceedings(title, author, booktitle, year)
        update_inproceedings_citation(id, title, author, booktitle, year)
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

    try:
        validate_article(title, author, journal, year)
        update_article_citation(id, title, author, journal, year)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect(f"/edit_citation/{id}")


@app.route("/delete_citations", methods=["POST"])
def delete_citations():
    for citation_id in request.form.getlist("citation_id"):
        try:
            delete_citation(citation_id)
        except Exception as error:
            flash(str(error))
            return redirect("/")
    return redirect("/")

@app.route("/", methods=["GET","POST"])
def get_bibtex():
    bibtex_results = []
    if request.method == "POST":
        for citation in get_all_citations():
            bibtex = get_bibtex_citation(citation.id)
            bibtex_results.append(bibtex)
    return render_template("index.html", bibtex_results=bibtex_results, book_citations=get_all_citations())


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db", methods=["POST"])
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
