use class_db;
select count(distinct p.city, p.country) from Affiliations a, Place p where a.affiliationName="University of California" and a.pid=p.id;
