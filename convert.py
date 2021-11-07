import json

# load data
# data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))
data = json.load(open("/home/cs143/shared/project3/CS143-Project3/data/nobel-laureates.json", "r"))
#data = json.load(open("/home/cs143/shared/proj3/data/nobel-laureates.json", "r"))
delimiter = "$"

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

def makePlaceID(city, country):
    return hash(city + ", " + country) % 2147483647

def loadDelFiles(laureateSet, personSet, placeSet, organizationSet, birthSet, prizeSet, affiliationSet):
    d = dict()
    d["laureate"] = laureateSet
    d["person"] = personSet
    d["place"] = placeSet
    d["organization"] = organizationSet
    d["birth"] = birthSet 
    d["prize"] = prizeSet
    d["affiliations"] = affiliationSet

    for k, v in d.items():
        filename = k + ".del"
        tupSet = v
        # print (f"Loading {filename}...")
        with open(filename, "w") as fd:
            for tup in tupSet:
                line = ""
                for col in tup:
                    line += str(col) + delimiter
                line = line + "\n"
                fd.write(line)

def handleData(data):
    # affiliate ids - just hash the name of the affiliate
    # place id - just hash the tuple of the (city, country)
    pid = 0 # prize id - have a counter of how many prizes seen so far
    debug = False 
    laureateSet = set()
    personSet = set()
    organizationSet = set()
    birthSet = set()
    placeSet = set()
    prizeSet = set()
    affiliationSet = set()
    for ind, laureate in enumerate(data["laureates"]):
        if debug: print ("-------")
        if "orgName" in laureate:
            attrVals = [["id"], ["orgName", "en"],
                    ["founded", "date"], ["founded", "place", "city", "en"], ["founded", "place", "country", "en"],
                    ["nobelPrizes"]]
            attrKeys = ["id", "orgName", "birthDate", "birthCity", "birthCountry", "nobelPrizes"]
            attrs = dict()
            for i in range(len(attrKeys)):
                attrs[attrKeys[i]] = get(laureate, attrVals[i])
            attrs["nobelPrizes"] = parseNobelPrizes(attrs["nobelPrizes"])

            organizationTuple = (attrs["id"], attrs["orgName"])
            organizationSet.add(organizationTuple)

            placeID = makePlaceID(attrs["birthDate"], attrs["birthCountry"])
            placeTuple = (placeID, attrs["birthDate"], attrs["birthCountry"])
            placeSet.add(placeTuple)

            birthTuple = (attrs["id"], attrs["birthDate"], placeID)
            birthSet.add(birthTuple)


            # print (attrs["id"])
            for prize in attrs["nobelPrizes"]:
                laureateTuple = (attrs["id"], pid)
                laureateSet.add(laureateTuple)
                for affiliate in prize["affiliations"]:
                    # print (affiliate)
                    affiliateID = hash(affiliate["name"]) % 2147483647
                    prizeTuple = (pid, prize["awardYear"], prize["category"], prize["sortOrder"], affiliateID)
                    if debug: print (f"Prize: {prizeTuple}")
                    prizeSet.add(prizeTuple)

                    placeID = makePlaceID(affiliate["city"], affiliate["country"])
                    placeTuple = (placeID, affiliate["city"], affiliate["country"])
                    if debug: print(f"Affiliate Place: {placeTuple}")
                    placeSet.add(placeTuple)
                    affiliateTuple = (affiliateID, affiliate["name"], placeID)
                    if debug: print(f"Affiliate: {affiliateTuple}")
                    affiliationSet.add(affiliateTuple)
                pid += 1

        else:
            attrVals = [["id"], ["givenName", "en"], ["familyName", "en"], ["gender"],
                    ["birth", "date"], ["birth", "place", "city", "en"], ["birth", "place", "country", "en"],
                    ["nobelPrizes"]]
            attrKeys = ["id", "givenName", "familyName", "gender", "birthDate", "birthCity", "birthCountry", "nobelPrizes"]
            attrs = dict()
            for i in range(len(attrKeys)):
                attrs[attrKeys[i]] = get(laureate, attrVals[i])
            attrs["nobelPrizes"] = parseNobelPrizes(attrs["nobelPrizes"])


            personTuple = (attrs["id"], attrs["givenName"], attrs["familyName"], attrs["gender"])
            if debug: print (f"Person: {personTuple}")
            personSet.add(personTuple)

            placeID = makePlaceID(attrs["birthCity"], attrs["birthCountry"])
            placeTuple = (placeID, attrs["birthCity"], attrs["birthCountry"])
            placeSet.add(placeTuple)
            if debug: print (f"Birth Place: {placeTuple}")
            birthTuple = (attrs["id"], attrs["birthDate"], placeID)
            if debug: print (f"Birth: {birthTuple}")
            birthSet.add(birthTuple)
            print("Person: " + str(attrs["id"]))
            for prize in attrs["nobelPrizes"]:
                laureateTuple = (attrs["id"], pid)
                if debug: print (f"Laureate: {laureateTuple}")
                laureateSet.add(laureateTuple)
                print ("Prize:")
                for affiliate in prize["affiliations"]:
                    affiliateID = hash(affiliate["name"]) % 2147483647
                    prizeTuple = (pid, prize["awardYear"], prize["category"], prize["sortOrder"], affiliateID)
                    print (f"Prize: {prizeTuple}")
                    prizeSet.add(prizeTuple)

                    placeID = makePlaceID(affiliate["city"], affiliate["country"])
                    placeTuple = (placeID, affiliate["city"], affiliate["country"])
                    if debug: print(f"Affiliate Place: {placeTuple}")
                    placeSet.add(placeTuple)
                    affiliateTuple = (affiliateID, affiliate["name"], placeID)
                    print(f"Affiliate: {affiliateTuple}")
                    affiliationSet.add(affiliateTuple)

                pid += 1
        

    loadDelFiles(laureateSet, personSet, placeSet, organizationSet, birthSet, prizeSet, affiliationSet)



handleData(data)

# {print (f"{k} : {v}") for k, v in attrs.items() if k != "nobelPrizes"}
# {print (f"{k} : {v}") for k, v in attrs["nobelPrizes"][0].items()}
