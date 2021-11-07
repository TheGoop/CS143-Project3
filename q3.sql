select p.familyName from Laureates l, Person p where l.id=p.id group by familyName having count(familyName)>4;
