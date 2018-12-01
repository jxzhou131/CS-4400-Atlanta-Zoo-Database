#visitorSearchExhibit 
SELECT * FROM 
(SELECT E.Name as name, WaterFeature as feature, Size as size, COUNT(*) as Num FROM EXHIBIT as E, ANIMAL as A 
WHERE E.Name = A.Exhibit  AND E.name = 'Birds' AND WaterFeature = True  AND Size > 1 AND Size < 2000 GROUP BY E.Name) as t1 
WHERE Num > 1 AND Num < 5
ORDER BY name ASC #DESC

-- SELECT * FROM 
-- (SELECT E.Name as name, WaterFeature as feature, Size as size, COUNT(*) as Num FROM EXHIBIT as E, ANIMAL as A 
-- WHERE E.Name = A.Exhibit  
-- AND E.name = $E.name AND WaterFeature = $WaterFeature(True/False)  AND Size > $Size_min AND Size < $Size_max GROUP BY E.Name) as t1 
-- WHERE Num > $Num_min AND Num < $Num_max
-- ORDER BY $Attribute ASC #DESC