use class_db;
select distinct p.id from Laureates l inner join Person p on l.id=p.id and p.familyName="Curie" and p.givenName="Marie";
