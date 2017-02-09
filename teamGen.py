import random

def teamPicker():
    animals = ['Dragons', 'Lions', 'Cats', 'Lynxes', 'Tigers', 'Sharks', 'Jaguars', 'Panthers', 'Cobras', 'Bisons', 'Alligators', 'Scorpions', 'Honey-Badgers', 'Piranhas', 'Porcupines', 'Warthogs', 'Wolves', 'Zebras', 'Spiders', 'Vipers', 'Eagles', 'Gorillas']

    regions = ['britain', 'scandinavia', 'german']
    selected = random.choice(regions)
    teamname = random.choice(selected) + ' ' + random.choice(animals)

CITIES_BRITISH = ['London', 'Cardiff', 'Dublin', 'Edinburgh', 'Manchester', 'Southampton', 'Liverpool', 'Bristol', 'Leeds', 'Cambridge', 'Glasgow']
CITIES_SCANDINAVIAN = ['Copenhagen', 'Aarhus', 'Oslo' 'Bergen', 'Trondheim', 'Gothenburg', 'Malmö', 'Stockholm', 'Helsinki', 'Tampere', 'Jyväskylä', 'Reykjavík', 'Tórshavn']
CITIES_GERMAN = ['Berlin', 'Munich', 'Hamburg', 'Dortmund', 'Essen', 'Hanover', 'Bremen', 'Düsseldorf' 'Vienna', 'Salzburg', 'Graz', 'Bern', 'Zürich', 'Basel']