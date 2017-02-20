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
print("Now, you will get to draft your players! Hang on, generating players.")

BOYS = []

for i in range(60):
    peep = player()
    player_create(peep)