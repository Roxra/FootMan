import random
from lists import *

def team_picker(fc):
    regions = ['britain', 'scandinavia', 'german']

    # Choose random team region
    fc.city = random.choice(regions)

    # Select a random city, from the region selected
    if fc.city == 'britain':
        fc.name = rand_list_append(CITIES_BRITAIN, fc)
    elif fc.city == 'scandinavia':
        fc.name = rand_list_append(CITIES_SCANDINAVIA, fc)
    else:
        fc.name = rand_list_append(CITIES_GERMAN, fc)

def rand_list_append(region, fc):
    # Select a random mascot and city from
    # the previously selected region
    fc.mascot = random.choice(TEAM_MASCOTS)
    fc.city = random.choice(region)

    return(fc.city + ' ' + fc.mascot)
