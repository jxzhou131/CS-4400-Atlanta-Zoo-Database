-- adminViewShows

-- searchShows
SELECT Name, Location, DateTime from SHOWS
WHERE Name = $Name AND Location = $Location AND DateTime = $DateTime;

-- removeShows
DELETE FROM SHOWS
WHERE Name = $Name AND DateTime= STR_TO_DATE($DateTime , '%m/%d/%Y %r');