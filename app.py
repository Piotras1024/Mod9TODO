from flask import Flask, request, render_template, redirect, url_for

from forms import Domowe_wydatkiForm
from models import domowe_wydatki

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/domowe_wydatki/", methods=["GET", "POST"])
def wydatki_list():
    form = Domowe_wydatkiForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            domowe_wydatki.create(form.data)
            domowe_wydatki.save_all()
        return redirect(url_for("wydatki_list"))

    return render_template("domowe_wydatki.html", form=form, domowe_wydatki=domowe_wydatki.all(), error=error)


@app.route("/domowe_wydatki/<int:domowe_wydatki_id>/", methods=["GET", "POST"])
def wydatki_details(domowe_wydatki_id):
    dom_wydatki = domowe_wydatki.get(domowe_wydatki_id - 1)
    form = Domowe_wydatkiForm(data=dom_wydatki)

    if request.method == "POST":
        if form.validate_on_submit():
            domowe_wydatki.update(domowe_wydatki_id - 1, form.data)
        return redirect(url_for("wydatki_list"))
    return render_template("dom_wydatki.html", form=form, domowe_wydatki_id=domowe_wydatki_id)


