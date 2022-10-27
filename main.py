from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy, sqlalchemy

from data.teams import Team

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://nfl.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def home():

    teams = Team.query
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="81")
