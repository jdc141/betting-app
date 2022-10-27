from data.base_model import db

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.Integer, db.ForeignKey('team.id'))
    away_team = db.Column(db.Integer, db.ForeignKey('team.id'))
