--AnimalCare Page
--import_main_

--Intial view of the AnimalCare Page
--show Staff Member, Note, DateTime
SELECT Staff, Text, DateTime
FROM Note
WHERE AnimalName = '' AND AnimalSpecies = ''


--When LogNote is Press
--Insert a tuble

INSERT INTO NOTE(Staff,AnimalName, AnimalSpecies, DateTime,Text)
VALUES (_main_loginIdentitiy[0], 'AnimalName', 'AnimalSpecies', 'DateTime', 'Note')
