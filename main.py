from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from data.data_models import Team

from data.onetimeload import add_teams


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nfl.sqlite3'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

@app.route("/")
def home():

    add_teams()
    teams = Team.query
    print(teams)
    return render_template("index.html", team=teams)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="0.0.0.0", port="81")
