-- StaffViewShows
-- Staff member should see all shows for which an admin has assigned them to host
-- Time of shows
-- Name of show
-- Exhibit the show is located in
-- import_main_



-- SELECT Name, DateTime,Location
-- FROM SHOWS
-- WHERE Host = $Host and Name = $Name
-- and DateTime = $DateTime and Location = $Location
-- ORDER BY $Attribute $ASC/DESC;


SELECT Name, DateTime,Location
FROM SHOWS
WHERE Host = 'benjamin_rao' and Name = 'Climbing' 
and DateTime = STR_TO_DATE('10/10/18 4:00:00 PM','%m/%d/%Y %r') and Location = 'Mountainous'
ORDER BY DateTime DSC;
