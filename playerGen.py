import random
from teamGen import *

def player_name_gen(city):
    british_first = ['David', 'William', 'Robert', 'Daniel', 'John', 'James', 'Micheal', 'Paul', 'Mark']
    british_last = ['Smith', 'Johnson', 'Williams', 'Browns', 'Wilson', 'Moore', 'Anderson']

    nordic_first = ['Juni', 'Jarel', 'Hjalmar', 'Havelock', 'Hedvig', 'Osvald', 'Ulf', 'Tyw']
    nordic_last = ['Jensen', 'Nielsen', 'Hansen', 'Larsen', 'Lund', 'Holm', 'Vestergaard']

    german_first = ['Stefan', 'Lukas', 'Niklas', 'Luis', 'Leon', 'Jonas', 'Finn', 'Max', 'Ben', 'Jakob']
    german_last = ['Schmidt', 'Schneider', 'Fischer', 'Weber', 'Meyer', 'Becker', 'Klein']

    if city in CITIES_BRITAIN:
        name = player_name_randomise(british_first, british_last)
    elif city in CITIES_SCANDINAVIA:
        name = player_name_randomise(nordic_first, nordic_last)
    elif city in CITIES_GERMAN:
        name = player_name_randomise(german_first, german_last)
    return name

def player_name_randomise(first, last):
    name = random.choice(first) + ' ' + random.choice(last)
    return name