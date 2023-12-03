from flask import Flask, render_template, request, redirect
from markupsafe import escape

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle the form submission logic here if needed
        pass
    return render_template("index.html")

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='127.0.0.1', port=80)
