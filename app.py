from flask import Flask, render_template, request
from parser import (
    parse_grammar,
    remove_epsilon,
    remove_unit,
    remove_useless,
    to_cnf
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    grammar = ""
    parsed = {}
    no_epsilon = {}
    no_unit = {}
    no_useless = {}
    cnf = {}

    if request.method == "POST":
        grammar = request.form["grammar"]

        parsed = parse_grammar(grammar)
        no_epsilon = remove_epsilon(parsed)
        no_unit = remove_unit(no_epsilon)
        no_useless = remove_useless(no_unit)
        cnf = to_cnf(no_useless)

    return render_template(
        "index.html",
        grammar=grammar,
        parsed=parsed,
        no_epsilon=no_epsilon,
        no_unit=no_unit,
        no_useless=no_useless,
        cnf=cnf
    )

if __name__ == "__main__":
    app.run(debug=True)