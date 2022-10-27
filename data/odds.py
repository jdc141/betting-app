from data.base_model import db

class Odds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.home_team'))
    home_spread = db.Column(db.Float)
    away_team = db.Column(db.Integer, db.ForeignKey('schedule.away_team'))
    away_spread = db.Column(db.Float)
    total = db.Column(db.Float)
