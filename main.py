from datetime import date
from unicodedata import name
from flask import Flask, render_template
import requests
from flask_sqlalchemy import SQLAlchemy, sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://nfl.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.Integer, db.ForeignKey('team.id'))
    away_team = db.Column(db.Integer, db.ForeignKey('team.id'))


class Odds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.home_team'))
    home_spread = db.Column(db.Float)
    away_team = db.Column(db.Integer, db.ForeignKey('schedule.away_team'))
    away_spread = db.Column(db.Float)
    total = db.Column(db.Float)


@app.route("/")
def home():

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="81")
