from flask import Flask, render_template, request
from parser import parse_grammar, remove_epsilon

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    grammar = ""
    parsed = {}
    no_epsilon = {}

    if request.method == "POST":
        grammar = request.form["grammar"]
        parsed = parse_grammar(grammar)
        no_epsilon = remove_epsilon(parsed)

    return render_template(
        "index.html",
        grammar=grammar,
        parsed=parsed,
        no_epsilon=no_epsilon
    )

if __name__ == "__main__":
    app.run(debug=True)