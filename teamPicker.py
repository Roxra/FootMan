import random

def teamPicker():

    #Teams = ['Tirana', 'Vienna', 'Brussels', 'Sofia', 'Prague', 'Tallinn', 'Berlin', 'Helsinki', 'Athens', 'Budapest', 'Dublin', 'Rome', ' Kosovo', 'Vaduz', 'Luxembourg', 'Valletta', 'Amsterdam', 'Monaco', 'Warsaw', 'Bucharest', 'San Marino', 'Bratislava', 'Madrid', 'Berne', 'London', 'Vatican City', 'Kiev', 'Stockholm', 'Ljubljana', 'Belgrade', 'Moscow', 'Oslo', 'Podgorica', 'Chisinau', 'Skopje', 'Vilnius', 'Riga', 'Saint Heller', 'Douglas', 'Reykjavik', 'Gibraltar', 'Paris', 'Tórshavn', 'Copenhagen', 'Zagreb', 'Sarajevo', 'Minsk', 'Tbilisi', 'Cardiff']
    
    britain = ['London', 'Cardiff', 'Dublin', 'Edinburgh']
    
    balkans = ['Tirana', 'Sofia', 'Belgrade', 'Zagreb', 'Ljubljana', 'Sarajevo', 'Rome', 'Bucharest', 'Tirana', 'Ankara', 'Athens']
    
    scandinavia = ['Copenhagen', 'Oslo', 'Stockholm', 'Helsinki', 'Reykjavík'] #I have not added all the ones you origanlly wrote in teams yet
    
    germanic = ['Berlin', 'Vienna']
    
    animals = ['Dragons', 'Lions', 'Cats', 'Lynxes', 'Tigers', 'Sharks', 'Jaguars', 'Panthers', 'Cobras', 'Bisons', 'Alligators', 'Scorpions', 'Honey-Badgers', 'Piranhas', 'Porcupines', 'Warthogs', 'Wolves', 'Zebras', 'Spiders', 'Vipers', 'Eagles', 'Gorillas']

    britainteamname = random.choice(britain) + ' ' + random.choice(animals)
    balkansteamname = random.choice(balkans) + ' ' + random.choice(animals)
    scandinaviateamname = random.choice(scandinavia) + ' ' + random.choice(animals)
    worldwideteamname = random.choice(britain+balkans+scandinavia) + ' ' + random.choice(animals)
                   
    return worldwideteamname
                   
    #i guess we need some sort of input for what nationality you want? or is it just going to be random and the nationality is left "behind the scenes"?
