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

