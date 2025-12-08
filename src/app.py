from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from config import app, test_env

from entities.citation_types import CitationTypes

from repositories.citation_repository import CitationRepository
from repositories.tags_repository import TagRepository

from services.citation_service import CitationService
from services.bibtex_service import BibtexService
from services.validator_service import InputValidation


tag_repo = TagRepository()
citation_repo = CitationRepository(tag_repo)
validator = InputValidation()
citation_service = CitationService(citation_repo, tag_repo, validator)
bibtex_service = BibtexService(citation_repo)


@app.route("/")
def index():
    selected_tags = request.args.getlist("tag")
    match_all = request.args.get("match_all", "false").lower() == "true"
    all_tags = tag_repo.get_all_tags()

    if selected_tags:
        citations = citation_repo.get_citations_by_tag(selected_tags, match_all=match_all)
    else:
        citations = citation_repo.get_all_citations()

    return render_template(
        "index.html",
        citations=citations,
        tags=all_tags,
        selected_tags=selected_tags,
        match_all=match_all
    )

@app.route("/new_citation")
def new():
    return render_template("new_citation.html")

@app.route("/create_book_citation", methods=["POST"])
def citation_creation_book():
    try:
        citation_service.create_citation(CitationTypes.BOOK.value, request.form)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_citation")

@app.route("/create_inproceedings_citation", methods=["POST"])
def citation_creation_inproceedings():
    try:
        citation_service.create_citation(CitationTypes.INPROCEEDINGS.value, request.form)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_citation")

@app.route("/create_article_citation", methods=["POST"])
def citation_creation_article():
    try:
        citation_service.create_citation(CitationTypes.ARTICLE.value, request.form)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_citation")

@app.route("/edit_citation/<int:id>")
def edit_citation(id):
    citation = citation_repo.get_citation(id)
    if citation is None:
        return redirect("/")

    return render_template("edit_citation.html", citation=citation)

@app.route("/edit_book_citation/<int:id>", methods=["POST"])
def citation_edition_book(id):
    try:
        citation_service.update_citation(id, CitationTypes.BOOK.value, request.form)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect(f"/edit_citation/{id}")

@app.route("/edit_inproceedings_citation/<int:id>", methods=["POST"])
def citation_edition_inproceedings(id):
    try:
        citation_service.update_citation(id, CitationTypes.INPROCEEDINGS.value, request.form)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect(f"/edit_citation/{id}")

@app.route("/edit_article_citation/<int:id>", methods=["POST"])
def citation_edition_article(id):
    try:
        citation_service.update_citation(id, CitationTypes.ARTICLE.value, request.form)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect(f"/edit_citation/{id}")

@app.route("/delete_citations", methods=["POST"])
def delete_citations():
    try:
        citation_service.delete_citation(request.form)
    except Exception as error:
        flash(str(error))
        return redirect("/")
    return redirect("/")

@app.route("/bibtex", methods=["GET","POST"])
def get_bibtex():
    bibtex_results = []
    for citation in citation_repo.get_all_citations():
        bibtex = bibtex_service.get_bibtex_citation(citation.id)
        bibtex_results.append(bibtex)

    return render_template("bibtex.html", bibtex_results=bibtex_results)

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db", methods=["POST"])
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
