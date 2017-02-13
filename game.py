from teamGen import *
from playerGen import *

class club:
    def __init__(self):
        self.name = ''
        self.city = ''
        self.mascot = ''
        self.players = []

# Initialise clubs
team1 = club()
team2 = club()

# Send clubs to team_picker to add city and team name
team_picker(team1)
team_picker(team2)

print("For today's match, we have " + team1.name + " facing " + team2.name)

# for i in range (0, 40):
#     team1.players.append()
