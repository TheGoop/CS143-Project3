import json

# load data
# data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))
data = json.load(open("/home/cs143/shared/proj3/data/nobel-laureates.json", "r"))


class Place:
    def __init__(self, place = None):
        if place:
            if "city" in place:
                self.city = place["city"]["en"]
            else:
                self.city = None 
            if "country" in place:
                self.country = place["country"]["en"]
            else:
                self.country = None 
        else:
            self.city = None
            self.country = None 

    def __repr__(self):
        return self.city + ", " + self.country

class Birth:
    def __init__(self, birth = None):
        if birth:
            self.birthDate = birth["date"]
            self.place = Place(birth["place"])
        else:
            self.birthDate = None 
            self.place = Place()

class Affiliation:
    def __init__(self, affiliation):
        self.name = affiliation["name"]["en"]
        self.place = Place(affiliation)

class NobelPrize:
    def __init__(self, nobelPrize):
        self.awardYear = nobelPrize["awardYear"]
        self.category = nobelPrize["category"]
        self.sortOrder = nobelPrize["sortOrder"]
        if "affiliations" in nobelPrize:
            self.affiliations = [Affiliation(i) for i in nobelPrize["affiliations"]]
        else:
            self.affiliations = None

    def __repr__(self):
        s = f"year : {self.year} \n"
        s += f"category : {self.category} \n"
        s += f"sortOrder : {self.sortOrder} \n"
        for i in self.affiliations:
            s += f"affiliation : {self.affiliation} \n"
        

class OrgLaureate:
    pass

class PersonLaureate:
    def __init__(self, laureate):
        if "orgName" in laureate:
            raise Exception(f"Invalid type given here: {laureate}")
        self.id = laureate["id"]
        self.givenName = laureate["givenName"]["en"]
        if "familyName" in laureate:
            self.familyName = laureate["familyName"]["en"]
        else:
            self.familyName = None 
        self.gender = laureate["gender"]
        if "birth" in laureate:
            self.birth = Birth(laureate["birth"])
        else:
            self.birth = Birth()
        self.nobelPrizes = [NobelPrize(i) for i in laureate["nobelPrizes"]]
        
def checkPersonLaureate(laureate):
    personLaureate = PersonLaureate(laureate)
    assert(personLaureate.id == laureate["id"] and personLaureate.id)
    assert(personLaureate.givenName == laureate["givenName"]["en"] and personLaureate.givenName)\
    # assert(personLaureate.familyName == laureate["familyName"]["en"] and personLaureate.familyName)
    assert(personLaureate.gender == laureate["gender"] and personLaureate.gender)
    assert(personLaureate.birth.birthDate == laureate["birth"]["date"] and personLaureate.birth.birthDate)
    # assert(personLaureate.birth.place.city == laureate["birth"]["place"]["city"]["en"] and personLaureate.birth.place.city)
    # assert(personLaureate.birth.place.country == laureate["birth"]["place"]["country"]["en"] and personLaureate.birth.place.country)
    assert(len(personLaureate.nobelPrizes) == len(laureate["nobelPrizes"]))
    for i in range(len(laureate["nobelPrizes"])):
        nobelPrize = personLaureate.nobelPrizes[i]
        assert(nobelPrize.awardYear == laureate["nobelPrizes"][i]["awardYear"] and nobelPrize.awardYear)
        assert(nobelPrize.category == laureate["nobelPrizes"][i]["category"] and nobelPrize.category)
        assert(nobelPrize.sortOrder == laureate["nobelPrizes"][i]["sortOrder"] and nobelPrize.sortOrder)
        # for j in range(len(laureate["nobelPrizes"][i]["affiliations"])):
        #     affiliationObj = nobelPrize.affiliations[j]
            # affiliation = laureate["nobelPrizes"][i]["affiliations"][j] 
            # assert(affiliationObj.name == affiliation["name"]["en"] and affiliationObj.name)
            # assert(affiliationObj.place.city == affiliation["city"]["en"] and affiliationObj.place.city)
            # assert(affiliationObj.place.country == affiliation["country"]["en"] and affiliationObj.place.country)



# get the id, givenName, and familyName of the first laureate
for i, laureate in enumerate(data["laureates"]):
    print (laureate["id"])
    if "orgName" not in laureate:
        checkPersonLaureate(laureate)

