--StaffViewShows
--Staff member should see all shows for which an admin has assigned them to host
-- Time of shows
--Name of show
--Exhibit the show is located in
--import_main_


SELECT Name, DateTime,Location
FROM SHOWS
WHERE Host = 'martha_johnson'
