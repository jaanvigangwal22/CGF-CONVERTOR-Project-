from flask import Flask, render_template, request
from parser import (
    parse_grammar,
    remove_epsilon,
    remove_unit,
    remove_useless,
    to_cnf,
    gnf_steps,
    format_grammar
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    original = ""
    epsilon = ""
    unit = ""
    useless = ""
    cnf = ""
    gnf_step1 = ""
    gnf_step2 = ""
    gnf = ""

    if request.method == "POST":

        grammar = request.form["grammar"]

        parsed = parse_grammar(grammar)
        no_epsilon = remove_epsilon(parsed)
        no_unit = remove_unit(no_epsilon)
        no_useless = remove_useless(no_unit)
        cnf_rules = to_cnf(no_useless)

        step1, step2, final = gnf_steps(cnf_rules)

        original = format_grammar(parsed)
        epsilon = format_grammar(no_epsilon)
        unit = format_grammar(no_unit)
        useless = format_grammar(no_useless)
        cnf = format_grammar(cnf_rules)
        gnf_step1 = format_grammar(step1)
        gnf_step2 = format_grammar(step2)
        gnf = format_grammar(final)

    return render_template(
        "index.html",
        original=original,
        epsilon=epsilon,
        unit=unit,
        useless=useless,
        cnf=cnf,
        gnf_step1=gnf_step1,
        gnf_step2=gnf_step2,
        gnf=gnf
    )

if __name__ == "__main__":
    app.run(debug=True)