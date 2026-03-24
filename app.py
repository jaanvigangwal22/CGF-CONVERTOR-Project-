from flask import Flask, render_template, request
from parser import parse_grammar

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    grammar = ""
    parsed = {}

    if request.method == "POST":
        grammar = request.form["grammar"]
        parsed = parse_grammar(grammar)

    return render_template("index.html", grammar=grammar, parsed=parsed)

if __name__ == "__main__":
    app.run(debug=True)