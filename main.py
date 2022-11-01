from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    con = sqlite3.connect("nfl.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT name FROM team")

    rows = cur.fetchall()
    return render_template("index.html", rows = rows)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="81")
