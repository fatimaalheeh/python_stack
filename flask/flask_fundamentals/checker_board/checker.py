from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/<rows>')
def oneindex(rows, columns=8):
    return render_template("changeindex.html", rows=int(rows), columns=int(columns))
    return render_template("index.html")

@app.route('/<rows>/<columns>')
def changed(rows, columns):
    return render_template("changeindex.html", rows=int(rows), columns=int(columns))

if __name__=="__main__":
    app.run(debug=True)