

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