use class_db;
drop table if exists Laureates;
drop table if exists Person;
drop table if exists Organization;
drop table if exists Birth;
drop table if exists Place;
drop table if exists Prize;
drop table if exists Affiliations;

create table Laureates(
    id int,
    nid int
);

create table Person(
    id int primary key, 
    givenName varchar(255),
    familyName varchar(255),
    gender varchar(6) -- we only have male/female in our data
);

create table Organization(
    id int primary key, 
    orgName varchar(255)
);

create table Birth(
    id int primary key,
    birthdate date, 
    pid int
);

create table Place(
    id int primary key, 
    city varchar(255),
    country varchar(255)
);

create table Prize(
    id int, 
    year int, 
    category varchar(255),
    sortOrder int, 
    aid int
);

create table Affiliations(
    id int primary key, 
    affiliationName varchar(255),
    pid int
);

load data local infile './laureate.del' into table Laureates fields terminated by '$';
load data local infile './birth.del' into table Birth fields terminated by "$";
load data local infile './organization.del' into table Organization fields terminated by "$";
load data local infile './person.del' into table Person fields terminated by "$";
load data local infile './place.del' into table Place fields terminated by "$";
load data local infile './prize.del' into table Prize fields terminated by "$";
load data local infile './affiliations.del' into table Affiliations fields terminated by "$";

-- select id from Person where givenName = "Marie" and familyName = "Curie"; -- 1
-- select Country from Affiliations inner join Place on pid = Place.id where affiliationName = "CERN"; -- 2

