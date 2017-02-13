import random

# Pool of cities to choose from, grouped by region
CITIES_BRITAIN = ['London', 'Cardiff', 'Dublin', 'Edinburgh', 'Manchester', 'Southampton', 'Liverpool', 'Bristol', 'Leeds', 'Cambridge', 'Glasgow']
CITIES_SCANDINAVIA = ['Copenhagen', 'Aarhus', 'Oslo' 'Bergen', 'Trondheim', 'Gothenburg', 'Malmö', 'Stockholm', 'Helsinki', 'Tampere', 'Jyväskylä', 'Reykjavík', 'Tórshavn']
CITIES_GERMAN = ['Berlin', 'Munich', 'Hamburg', 'Dortmund', 'Essen', 'Hanover', 'Bremen', 'Düsseldorf' 'Vienna', 'Salzburg', 'Graz', 'Bern', 'Zürich', 'Basel']

TEAM_MASCOTS = ['Dragons', 'Lions', 'Cats', 'Lynxes', 'Tigers', 'Sharks', 'Jaguars', 'Panthers', 'Cobras', 'Bisons', 'Alligators', 'Scorpions', 'Honey-Badgers', 'Piranhas', 'Porcupines', 'Warthogs', 'Wolves', 'Zebras', 'Spiders', 'Vipers', 'Eagles', 'Gorillas']

def team_picker(fc):
    regions = ['britain', 'scandinavia', 'german']

    # Choose random team region, and assign mascot
    fc.city = random.choice(regions)
    fc.mascot = random.choice(TEAM_MASCOTS)

    # Select a random city, from the region selected
    if fc.city == 'britain':
        fc.city = random.choice(CITIES_BRITAIN)
    elif fc.city == 'scandinavia':
        fc.city = random.choice(CITIES_SCANDINAVIA)
    else:
        fc.city = random.choice(CITIES_GERMAN)

    fc.name = fc.city + ' ' + fc.mascot
