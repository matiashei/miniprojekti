from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.citation_repository import get_book_citations, create_book_citation
from config import app, test_env
from util import validate_book

@app.route("/")
def index():
    #citations = get_citations()
    #unfinished = len([citation for citation in citations])
    #return render_template("index.html", citations=citations, unfinished=unfinished)

    # Varmaan erittäin väliaikainen rakenne tässä:
    book_citations = get_book_citations()
    return render_template("index.html", book_citations=book_citations)


@app.route("/new_citation")
def new():
    return render_template("new_citation.html")

@app.route("/create_citation", methods=["POST"])
def citation_creation():
    title = request.form.get("title")
    author = request.form.get("author")
    publisher = request.form.get("publisher")
    isbn = request.form.get("ISBN")
    year = request.form.get("year")

    try:
        validate_book(title, author, publisher, isbn, year)
        create_book_citation(title, author, publisher, isbn, year)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_citation")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db", methods=["POST"])
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
