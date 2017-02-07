import random

def teamPicker():
    teams = ['Tirana', 'Vienna', 'Brussels', 'Sofia', 'Prague', 'Tallinn', 'Berlin', 'Helsinki', 'Athens', 'Budapest', 'Dublin', 'Rome', ' Kosovo', 'Vaduz', 'Luxembourg', 'Valletta', 'Amsterdam', 'Monaco', 'Warsaw', 'Bucharest', 'San Marino', 'Bratislava', 'Madrid', 'Berne', 'London', 'Vatican City', 'Kiev', 'Stockholm', 'Ljubljana', 'Belgrade', 'Moscow', 'Oslo', 'Podgorica', 'Chisinau', 'Skopje', 'Vilnius', 'Riga', 'Saint Heller', 'Douglas', 'Reykjavik', 'Gibraltar', 'Paris', 'Tórshavn', 'Copenhagen', 'Zagreb', 'Sarajevo', 'Minsk', 'Tbilisi', 'Cardiff']

    animals = ['Dragons', 'Lions', 'Cats', 'Lynxes', 'Tigers', 'Sharks', 'Jaguars', 'Panthers', 'Cobras', 'Bisons', 'Alligators', 'Scorpions', 'Honey-Badgers', 'Piranhas', 'Porcupines', 'Warthogs', 'Wolves', 'Zebras', 'Spiders', 'Vipers', 'Eagles', 'Gorillas']

    teamname = random.choice(teams) + ' ' + random.choice(animals)

    return teamname
