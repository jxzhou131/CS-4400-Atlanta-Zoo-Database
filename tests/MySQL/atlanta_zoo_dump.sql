-- DROP SCHEMA IF EXISTS ATLANTA_ZOO;
-- CREATE SCHEMA ATLANTA_ZOO;
USE ATLANTA_ZOO;

-- DROP ALL THE TABLES AND PREPOPULATE THE DATABASE WITH INITIAL DATA
-- DROP ALL THE TABLES
Drop table if exists `VISITEXHIBIT`;
Drop table if exists `VISITSHOWS`;
Drop table if exists `SHOWS`;
Drop table if exists `NOTE`;
Drop table if exists `ANIMAL`;
Drop table if exists `EXHIBIT`;
Drop table if exists `STAFF`;
Drop table if exists `VISITOR`;
Drop table if exists `ADMINS`;
Drop table if exists `USER`;

-- RECREATE ALL THE TABLES
CREATE TABLE USER(
Username varchar(30)  not null,
Password char(32)  not null, -- Using MD5 hash function
Email varchar(50)  not null,
UserType varchar(30) not null,
primary key(Username),
unique(Email)
)ENGINE = INNODB;


CREATE TABLE ADMINS(
AUsername varchar(30)  not null,
primary key(AUsername),
foreign key(AUsername) references USER(Username)
)ENGINE = INNODB;

CREATE TABLE VISITOR(
VUsername varchar(30)   not null,
primary key(VUsername),
foreign key(VUsername) references USER(Username)
       on delete cascade    on update cascade
)ENGINE = INNODB;

CREATE TABLE STAFF(
SUsername varchar(30)    not null,
primary key(SUsername),
foreign key(SUsername) references USER(Username)
       on delete cascade    on update cascade
)ENGINE = INNODB;

CREATE TABLE EXHIBIT(
Name varchar(30) not null,
WaterFeature boolean not null,
Size int    not null,
primary key(Name)
)ENGINE = INNODB;

CREATE TABLE ANIMAL(
Name varchar(30)   not null,
Species varchar(30)   not null,
Type varchar(15)   not null,
Age int     not null,
Exhibit varchar(30)     not null,
primary key(Name,Species),
foreign key(Exhibit) references EXHIBIT(Name)
	On delete cascade    on update cascade
)ENGINE = INNODB;

CREATE TABLE NOTE(
Staff varchar(30)     not null,
AnimalName varchar(30)    not null,
AnimalSpecies varchar(30)    not null,
DateTime datetime    not null,
Text varchar(200)    not null,
primary key(Staff, AnimalName, AnimalSpecies, DateTime),
foreign key(Staff) references STAFF(SUsername)
	on delete cascade    on update cascade,
foreign key(AnimalName, AnimalSpecies) references ANIMAL(Name, Species)
	on delete cascade   on update cascade
)ENGINE = INNODB;

CREATE TABLE SHOWS(
Name varchar(50)   not null,
DateTime datetime    not null,
Host varchar(30)   not null,
Location varchar(30)   not null,
primary key(Name,DateTime),
foreign key(Location) references EXHIBIT(Name)
on delete cascade    on update cascade,
foreign key(Host) references STAFF(SUsername)
      on delete cascade    on update cascade
)ENGINE = INNODB;

CREATE TABLE VISITSHOWS(
Visitor varchar(30) not null,
ShowName varchar(30) not null,
DateTime datetime not null,
primary key(Visitor, ShowName, DateTime),
foreign key(Visitor) references VISITOR(VUsername)
on delete cascade	   on update cascade,
foreign key(ShowName, DateTime) references SHOWS(Name, DateTime)
	On delete cascade    on update cascade
)ENGINE = INNODB;

CREATE TABLE VISITEXHIBIT(
Visitor varchar(30) not null,
ExhibitName varchar(30) not null,
DateTime datetime not null,
primary key(Visitor, ExhibitName, DateTime),
foreign key(Visitor) references VISITOR(VUsername)
      On delete cascade    on update cascade,
foreign key(ExhibitName) references EXHIBIT(Name)
	On delete cascade    on update cascade
)ENGINE = INNODB;

-- PREPOPULATE THE TABLES
-- LOCK TABLES `USER` WRITE;
INSERT INTO  `USER` 
VALUES ('martha_johnson', md5('password1'), 'marthajohnson@hotmail.com', 'staff'),
('benjamin_rao', md5('password2'), 'benjaminrao@gmail.com', 'staff'),
('ethan_roswell', md5('password3'), 'ethanroswell@yahoo.com', 'staff'),
('xavier_swenson', md5('password4'), 'xavierswenson@outlook.com', 'visitor'),
('isabella_rodriguez', md5('password5'), 'isabellarodriguez@mail.com', 'visitor'),
('nadias_tevens', md5('password6'), 'nadiastevens@gmail.com', 'visitor'),
('robert_bernheardt', md5('password7'), 'robertbernheardt@yahoo.com', 'visitor'),
('admin1', md5('adminpassword'), 'adminemail@mail.com', 'admin');
-- UNLOCK TABLES;

INSERT INTO `STAFF`
VALUES ('martha_johnson'), ('benjamin_rao'),('ethan_roswell');

INSERT INTO `VISITOR`
VALUES ('xavier_swenson'), ('isabella_rodriguez'),('nadias_tevens'),('robert_bernheardt');

INSERT INTO `ADMINS`
VALUES ('admin1');

INSERT INTO `EXHIBIT`
VALUES ('Pacific', True, 850), ('Jungle', False, 600), ('Sahara', False, 1000), ('Mountainous', False , 1200), ('Birds', True, 1000);


INSERT INTO `SHOWS`
VALUES 
('Jungle Cruise', 		STR_TO_DATE('10/6/2018 9:00:00 AM','%m/%d/%Y %r'), 	'martha_johnson', 	'Jungle'),
('Feed the Fish',		STR_TO_DATE('10/8/18 12:00:00 PM','%m/%d/%Y %r'),	'martha_johnson',	'Pacific'),
('Fun Facts',			STR_TO_DATE('10/9/18 3:00:00 PM','%m/%d/%Y %r'),	'martha_johnson',	'Sahara'),
('Climbing',			STR_TO_DATE('10/10/18 4:00:00 PM','%m/%d/%Y %r'),	'benjamin_rao'	,	'Mountainous'),
('Flight of the Birds',	STR_TO_DATE('10/11/18 3:00:00 PM','%m/%d/%Y %r'),	'ethan_roswell', 	'Birds'),
('Jungle Cruise',		STR_TO_DATE('10/12/18 2:00:00 PM','%m/%d/%Y %r'),	'martha_johnson',	'Jungle'),
('Feed the Fish',		STR_TO_DATE('10/12/18 2:00:00 PM','%m/%d/%Y %r'),	'ethan_roswell',	'Pacific'),
('Fun Facts',			STR_TO_DATE('10/13/18 1:00:00 PM','%m/%d/%Y %r'),	'benjamin_rao'	,	'Sahara'),
('Climbing',			STR_TO_DATE('10/13/18 5:00:00 PM','%m/%d/%Y %r'),	'benjamin_rao'	,	'Mountainous'),
('Flight of the Birds',	STR_TO_DATE('10/14/18 2:00:00 PM','%m/%d/%Y %r'),	'ethan_roswell'	,	'Birds'),
('Bald Eagle Show',		STR_TO_DATE('10/15/18 2:00:00 PM','%m/%d/%Y %r'),	'ethan_roswell'	,	'Birds')
 ;
 
 INSERT INTO `ANIMAL`
 VALUES
 ('Goldy',	'Goldfish'	,		'Fish'	,		12	,'Pacific'),
('Nemo'	,	'Clownfish'	,		'Fish'	,		24	,'Pacific'),
('Pedro',	'Poison Dart frog'	,'Amphibian',	36	,'Jungle'),
('Lincoln',	'Lion'	,			'Mammal'	,	96	,'Sahara'),
('Greg',	'Goat'	,			'Mammal'	,	72	,'Mountainous'),
('Brad',	'Bald Eagle'	,	'Bird'	,		48	,'Birds');

