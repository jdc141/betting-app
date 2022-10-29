from data.base_model import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

db.create_all()

# class Schedule(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     home_team = db.Column(db.Integer, db.ForeignKey('team.id'))
#     away_team = db.Column(db.Integer, db.ForeignKey('team.id'))

# class Odds(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.home_team'))
#     home_spread = db.Column(db.Float)
#     away_team = db.Column(db.Integer, db.ForeignKey('schedule.away_team'))
#     away_spread = db.Column(db.Float)
#     total = db.Column(db.Float)