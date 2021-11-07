select count(year) from (select distinct year from Laureates l, Organization o, Prize p where l.id=o.id and l.nid=p.id) as t;
