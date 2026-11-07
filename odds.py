import os
import requests
from dotenv import load_dotenv

#Load key from .env file
load_dotenv()
API_KEY = os.getenv("ODDS_API_KEY")

#Ask API for NBA moneyline odds from US sportsbooks
url = "https://api.the-odds-api.com/v4/sports/basketball_nba/odds"
params = {
    "apiKey" : API_KEY,
    "regions" : "us",
    "markets" : "h2h",
    "oddsFormat" : "decimal",
}
response = requests.get(url, params=params)

if response.status_code != 200:
    print("Something went wrong:", response.text)
else:
    games = response.json()
    for game in games:
        print(f"\n{game['away_team']} @ {game['home_team']}")
        for book in game["bookmakers"]:
            line = " " + book["title"] + ": "
            for outcome in book["markets"][0]["outcomes"]:
                line += f"{outcome['name']} {outcome['price']}x  "

            print(line)
