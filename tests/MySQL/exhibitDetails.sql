

#exhibitDetails

#exhibit details: display animal table 
SELECT Name, Species FROM ANIMAL 
WHERE Exhibit = 'Birds'
ORDER BY Species ASC #DESC

-- SELECT Name, Species FROM ANIMAL 
-- WHERE Exhibit = $Exhibit
-- ORDER BY $Attribute ASC #DESC



#exhibit details: dispaly size
SELECT Size FROM EXHIBIT 
WHERE Name = 'Pacific' 
-- SELECT Size FROM EXHIBIT 
-- WHERE Name = $Name 


#exhibit details: dispaly WaterFeature
SELECT WaterFeature FROM EXHIBIT 
WHERE Name = 'Pacific'
-- SELECT WaterFeature FROM EXHIBIT 
-- WHERE Name = $Name


#exhibit details: dispaly number of animals 
SELECT COUNT(*) FROM EXHIBIT as E, ANIMAL as A 
WHERE E.Name=A.Exhibit AND E.Name = 'Pacific'
GROUP BY E.Name

-- SELECT COUNT(*) FROM EXHIBIT as E, ANIMAL as A 
-- WHERE E.Name=A.Exhibit AND E.Name = $E.name
-- GROUP BY E.Name


SELECT * FROM((SELECT Name, WaterFeature, Size FROM EXHIBIT 
WHERE Name = 'Pacific') as ExhibitInfo
Natural Join
(SELECT E.Name, E.WaterFeature, E.Size, COUNT(*) as NumAnimals FROM EXHIBIT as E, ANIMAL as A 
WHERE E.Name=A.Exhibit AND E.Name = 'Pacific'
GROUP BY E.Name) as ExhibitCount)
ORDER BY NumAnimals;

-- SELECT * FROM((SELECT Name, WaterFeature, Size FROM EXHIBIT 
-- WHERE Name = $Name) as ExhibitInfo
-- Natural Join
-- (SELECT E.Name, E.WaterFeature, E.Size, COUNT(*) as NumAnimals FROM EXHIBIT as E, ANIMAL as A 
-- WHERE E.Name=A.Exhibit AND E.Name = $Name
-- GROUP BY E.Name) as ExhibitCount)
-- ORDER BY $Attribute;

insert into VISITEXHIBIT values('isabella_rodriguez','Flight of the Birds',STR_TO_DATE('10/11/18 3:00:00 PM','%m/%d/%Y %r'));

-- insert into VISITEXHIBIT values($Visitor,$ExhibitName,STR_TO_DATE($DateTime,'%m/%d/%Y %r'));
