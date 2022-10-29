from data.base_model import db
from data.data_models import Team 
import requests
import os

# original loading of teams in db - 10/27/2022


    
# json_obj = apiGrabber(
#     "https://odds.p.rapidapi.com/v4/sports/americanfootball_nfl/odds") 

# teamsList = teamNames(json_obj)

# add_teams()

def apiGrabber(url):
    # grabs api, uses env key 
    key = os.environ.get('LSO_API_KEY')

    querystring = {
        "oddsFormat": "american",
        "markets": "spreads,totals",
        "dateFormat": "iso",
        "bookmakers": "draftkings"
    }

    headers = {
	"X-RapidAPI-Key": key,
	"X-RapidAPI-Host": "odds.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    json_response = response.json()

    return json_response


def teamNames(json_obj):
    # takes teams from api and puts them in two lists 
    homeDict = {}
    awayDict = {}

    for index, team in enumerate(json_obj):
        if 'home_team' in team:
            homeDict[index] = team['home_team']

    for index, team in enumerate(json_obj):
        if 'away_team' in team:
            awayDict[index] = team['away_team']

    return [homeDict, awayDict]

def add_teams():
    # add teams into db
    # homeDict = teams[0]
    # awayDict = teams[1]
    # teamList = []
    teams = {
        0 : 'Arizona Cardinals',
        1 : 'Atlanta Falcons',
        2 : 'Baltimore Ravens',
        3 : 'Buffalo Bills',
        4 : 'Carolina Panthers',
        5 : 'Chicago Bears',
        6 : 'Cincinnati Bengals',
        7 : 'Cleveland Browns',
        8 : 'Dallas Cowboys',
        9 : 'Denver Broncos',
        10 : 'Detroit Lions',
        11 : 'Green Bay Packers',
        12 : 'Houston Texans',
        13 : 'Indianapolis Colts',
        14 : 'Jacksonville Jaguars',
        15 : 'Kansas City Chiefs',
        16 : 'Miami Dolphins',
        17 : 'Minnesota Vikings',
        18 : 'New England Patriots',
        19 : 'New Orleans Saints',
        20 : 'New York Giants',
        21 : 'New York Jets',
        22 : 'Las Vegas Raiders',
        23 : 'Philadelphia Eagles',
        24 : 'Pittsburgh Steelers',
        25 : 'Los Angeles Chargers',
        26 : 'San Francisco 49ers',
        27 : 'Seattle Seahawks',
        28 : 'Los Angeles Rams',
        29 : 'Tampa Bay Buccaneers',
        30 : 'Tennessee Titans',
        31 : 'Washington Commanders',
    }

    for i in teams:
        team = Team(name=i)
        db.session.add(team)
    db.session.commit()




