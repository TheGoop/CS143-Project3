import json

# load data
# data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))
data = json.load(open("/home/cs143/shared/proj3/data/nobel-laureates.json", "r"))
delimiter = ";"

def get(d, args):
    for arg in args:
        try: 
            d = d[arg]
        except:
            return 'null'
    return d


def parseAffiliations(affiliations):
    affs = []
    for affiliation in affiliations:
        aff = dict()
        attrs = [["name", "en"], ["city", "en"], ["country", "en"]]
        for attr in attrs: 
            aff[attr[0]] = get(affiliation, attr)
        affs.append(aff)
    return affs

def parseNobelPrizes(nobelPrizes):
    prizes = []
    for nobelPrize in nobelPrizes:
        prize = dict()
        attrs = [["awardYear"], ["category", "en"], ["sortOrder"], ["affiliations"]]
        for a in attrs:
            prize[a[0]] = get(nobelPrize, a)

        prize["affiliations"] = parseAffiliations(prize["affiliations"])
        prizes.append(prize)
    return prizes 


def handleData(data):
    # affiliate ids - just hash the name of the affiliate
    # place id - just hash the tuple of the (city, country)

    pid = 0 # prize id - have a counter of how many prizes seen so far
    laureates = person = organization = birth = place = prize = affiliations = set()
    # get the id, givenName, and familyName of the first laureate
    # for i, laureate in enumerate(data["laureates"]):
    laureate = data["laureates"][0]
    if "orgName" in laureate:
        pass
    else:
        attrVals = [["id"], ["givenName", "en"], ["familyName", "en"], ["gender"],
                ["birth", "date"], ["birth", "place", "city", "en"], ["birth", "place", "country", "en"],
                ["nobelPrizes"]]

        attrKeys = ["id", "givenName", "familyName", "gender", "birthDate", "birthCity", "birthCountry", "nobelPrizes"]
        attrs = dict()
        for i in range(len(attrKeys)):
            attrs[attrKeys[i]] = get(laureate, attrVals[i])
        
        attrs["nobelPrizes"] = parseNobelPrizes(attrs["nobelPrizes"])
        {print (f"{k} : {v}") for k, v in attrs.items() if k != "nobelPrizes"}
        {print (f"{k} : {v}") for k, v in attrs["nobelPrizes"][0].items()}
            
            
        


handleData(data)
        




    
        


    

