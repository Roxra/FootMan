from teamGen import *

class club:
    def __init__(self):
        self.name = ''
        self.city = ''
        self.mascot = ''

# Initialise clubs
team1 = club()
team2 = club()

# Send clubs to team_picker to add city and teamname
team_picker(team1)
team_picker(team2)

print("For today's match, we have " + team1.name + " facing " + team2.name)
