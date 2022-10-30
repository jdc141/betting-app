import sqlite3

con = sqlite3.connect("nfl.db")

cur = con.cursor()

teams = {
    0: 'Arizona Cardinals',
    1: 'Atlanta Falcons',
    2: 'Baltimore Ravens',
    3: 'Buffalo Bills',
    4: 'Carolina Panthers',
    5: 'Chicago Bears',
    6: 'Cincinnati Bengals',
    7: 'Cleveland Browns',
    8: 'Dallas Cowboys',
    9: 'Denver Broncos',
    10: 'Detroit Lions',
    11: 'Green Bay Packers',
    12: 'Houston Texans',
    13: 'Indianapolis Colts',
    14: 'Jacksonville Jaguars',
    15: 'Kansas City Chiefs',
    16: 'Miami Dolphins',
    17: 'Minnesota Vikings',
    18: 'New England Patriots',
    19: 'New Orleans Saints',
    20: 'New York Giants',
    21: 'New York Jets',
    22: 'Las Vegas Raiders',
    23: 'Philadelphia Eagles',
    24: 'Pittsburgh Steelers',
    25: 'Los Angeles Chargers',
    26: 'San Francisco 49ers',
    27: 'Seattle Seahawks',
    28: 'Los Angeles Rams',
    29: 'Tampa Bay Buccaneers',
    30: 'Tennessee Titans',
    31: 'Washington Commanders',
}

cur.execute("CREATE TABLE IF NOT EXISTS team(id INTEGER PRIMARY KEY, name TEXT)")

for i in range(len(teams)):
    cur.execute(" INSERT INTO team VALUES (?,?)", (i,teams[i],))

con.commit()
