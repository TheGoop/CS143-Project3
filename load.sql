use class_db;
drop table if exists Laureates;
drop table if exists Person;
drop table if exists Organization;
drop table if exists Birth;
drop table if exists Place;
drop table if exists Prize;
drop table if exists Affiliations;

create table Laureates(
    id int primary key,
    nid int not null
);

create table Person(
    id int primary key, 
    givenName varchar(255) not null,
    familyName varchar(255) not null,
    gender varchar(6) not null -- we only have male/female in our data
);

create table Organization(
    id int primary key, 
    orgName varchar(255) not null
);

create table Birth(
    id int primary key,
    birthdate date not null, 
    pid int not null
);

create table Place(
    id int primary key, 
    city varchar(255) not null,
    country varchar(255) not null
);

create table Prize(
    id int primary key, 
    year int not null, 
    category varchar(255) not null,
    sortOrder int not null, 
    aid int not null
);

create table Affiliations(
    id int primary key, 
    affiliationName varchar(255) not null,
    pid int  not null
);



