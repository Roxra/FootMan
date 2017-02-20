import teamGen as tG
import playerGen as pG
from header import *


class club:
    def __init__(self):
        self.name = UNDEF
        self.city = UNDEF
        self.mascot = UNDEF
        self.players = []

# Initialise clubs
team1 = club()
team2 = club()

# Send clubs to team_picker to add city and team name
tG.team_picker(team1)
tG.team_picker(team2)

print("For today's match, we have " + team1.name + " facing " + team2.name)
print("Now, you will get to draft your players! Hang on, generating players.")

BOYS = []

for i in range(60):
    peep = pG.player()
    pG.player_create(peep)
    BOYS.append(peep)

for i in BOYS:
    print(i.name + ' ' + i.city + ' ' + str(i.strength))
