#visitorSearchAnimals 
SELECT Name, Species, Exhibit, Type, Age FROM ANIMAL 
WHERE Name = 'Goldy' AND Species = 'Goldfish' AND Exhibit = 'Pacific' AND Type = 'Fish' AND Age > 1 AND Age < 30
ORDER BY Species ASC #DESC

-- SELECT Name, Species, Exhibit, Type, Age FROM ANIMAL 
-- WHERE Name = $Name AND Species = $Species AND Exhibit = $Exhibit AND Type = $Type AND Age > %Age_min AND Age < $Age_max
-- ORDER BY $Attribute ASC #DESC




