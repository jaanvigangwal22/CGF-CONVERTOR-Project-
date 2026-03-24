from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    grammar = ""

    if request.method == "POST":
        grammar = request.form["grammar"]

    return render_template("index.html", grammar=grammar)

if __name__ == "__main__":
    app.run(debug=True)