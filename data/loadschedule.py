import sqlite3
import requests
import os

con = sqlite3.connect("nfl.db")

cur = con.cursor()

key = os.environ.get('LSO_API_KEY')

url = "https://odds.p.rapidapi.com/v4/sports/americanfootball_nfl/odds"

querystring = {"regions": "us", "oddsFormat": "american",
               "markets": "spreads,totals", "dateFormat": "iso", "bookmakers": "draftkings"}

headers = {
    "X-RapidAPI-Key": key,
    "X-RapidAPI-Host": "odds.p.rapidapi.com"
}

response = requests.request(
    "GET", url, headers=headers, params=querystring)
json_response = response.json()

cur.execute("SELECT * FROM team")
rows = cur.fetchall()
# print(rows)

home_team = None
away_team = None
for item in json_response:
    for row in rows:
        if item['home_team'] in row[1]:
            home_team_id = row[0]
            home_team_name = item['home_team']
            home_team_spread = item['bookmakers'][0]['markets'][0]['outcomes'][0]['point']
            home_team_spread_price = item['bookmakers'][0]['markets'][0]['outcomes'][0]['price']
        if item['away_team'] in row[1]:
            away_team_id = row[0]
            away_team_name = item['away_team']
            away_team_spread= item['bookmakers'][0]['markets'][0]['outcomes'][1]['point']
            away_team_spread_price = item['bookmakers'][0]['markets'][0]['outcomes'][1]['price']
            total = item['bookmakers'][0]['markets'][1]['outcomes'][0]['point']
    cur.execute("INSERT INTO schedule (home_team_id, away_team_id) VALUES (?,?)", (home_team, away_team))

con.commit()


