from flask import Flask, render_template, request,redirect
from markupsafe import escape

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html",methods=["POST"])

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='127.0.0.1', port=80)
