-- AnimalCare Page
-- import_main_

-- Intial view of the AnimalCare Page
-- show Staff Member, Note, DateTime

-- SELECT Staff, Text, DateTime
-- FROM Note
-- WHERE AnimalName = $AnimalName AND AnimalSpecies = $AnimalSpecies
-- order by AnimalName;

SELECT Staff, Text, DateTime
FROM Note
WHERE AnimalName = 'Goldy' AND AnimalSpecies = 'Goldfish'
order by AnimalName;


-- When LogNote is Press
-- Insert a tuple


-- INSERT INTO NOTE(Staff,AnimalName, AnimalSpecies, DateTime,Text)
-- VALUES ($Staff, $AnimalName, $AnimalSpecies, $DateTime, $Text);


INSERT INTO NOTE(Staff,AnimalName, AnimalSpecies, DateTime,Text)
VALUES ('martha_johnson', 'Goldy', 'Goldfish', STR_TO_DATE('10/6/2018 9:00:00 AM','%m/%d/%Y %r'), 'Need more water');

INSERT INTO NOTE(Staff,AnimalName, AnimalSpecies, DateTime,Text)
VALUES ('benjamin_rao', 'Goldy', 'Goldfish', STR_TO_DATE('10/7/2018 9:00:00 AM','%m/%d/%Y %r'), 'Need more food');

INSERT INTO NOTE(Staff,AnimalName, AnimalSpecies, DateTime,Text)
VALUES ('xavier_swenson', 'Goldy', 'Goldfish', STR_TO_DATE('10/8/2018 9:00:00 AM','%m/%d/%Y %r'), 'Probably Dead');