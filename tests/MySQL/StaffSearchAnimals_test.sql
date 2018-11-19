--StaffSearchAnimals


--Search for all record
--no inputs, Exhibit/Type are select to ALL, Min == 0 and Max == 0
SELECT Name, Species, Exhibit, Age, Type
FROM ANIMAL

--Search for Animal with only specified Name, Exhibit, Type with Age Min < Max
SELECT Name, Species, Exhibit, Age, Type
FROM ANIMAL
WHERE Name = '' AND Exhibit = '' AND Type = '' AND Age <= 'Max.Age' AND Age >= Min.Age

--Search for Animal with only specified Name, Exhibit, Type with Age Min == Max
SELECT Name, Species, Exhibit, Age, Type
FROM ANIMAL
WHERE Name = '' AND Exhibit = '' AND Type = '' AND Age = 'Min.Age'

--Search for Animal with only specified Species, Exhibit, Type with Age Min < Max
SELECT Name, Species, Exhibit, Age, Type
FROM ANIMAL
WHERE Species = '' AND Exhibit = '' AND Type = '' AND Age <= 'Max.Age' AND Age >= Min.Age

--Search for Animal with only specified Species, Exhibit, Type with Age Min == Max
SELECT Name, Species, Exhibit, Age, Type
FROM ANIMAL
WHERE Species = '' AND Exhibit = '' AND Type = '' AND Age = 'Min.Age'

--Search for Animal with everything specified and Age Min < Max
SELECT Name, Species, Exhibit, Age, Type
FROM ANIMAL
WHERE Name = ''  AND Species = '' AND Exhibit = '' AND Type = '' AND Age <= 'Max.Age' AND Age >= 'Min.Age'

--Search for Animal with everything specified and Age Min = Max
SELECT Name, Species, Exhibit, Age, Type
FROM ANIMAL
WHERE Name = ''  AND Species = '' AND Exhibit = '' AND Type = '' AND Age == 'Min.Age'
