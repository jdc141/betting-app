import requests
import os

def main():

    json_obj = apiGrabber(
        "https://odds.p.rapidapi.com/v4/sports/americanfootball_nfl/odds")
    
    teamNames(json_obj)


    








def apiGrabber(url):

    key = os.environ.get('LSO_API_KEY')

    querystring = {
        "oddsFormat": "american",
        "markets": "spreads,totals", 
        "dateFormat": "iso",
        "bookmakers": "draftkings"
    }

    

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    json_response = response.json()

    return json_response

def teamNames(json_obj):

    homeDict = {}
    awayDict = {}

    for index, team in enumerate(json_obj):
        if 'home_team' in team:
            homeDict[index] = team['home_team']

    for index, team in enumerate(json_obj):
        if 'away_team' in team:
            awayDict[index] = team['away_team']

    return(homeDict, awayDict) 

if __name__ == "__main__":
    main()
