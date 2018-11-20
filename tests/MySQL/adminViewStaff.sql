-- search for all staff
-- if no input is specified
select Username, Email 
from USER u, STAFF s
where u.Username = s.SUsername and u.Usertype ="staff";

-- delete a specific staff from user
-- and staff table (will automatically get deleted since foreign key cascaded)
DELETE from USER
where Username = "martha_johnson" and Usertype = "staff";

DELETE from USER
where Username = "benjamin_rao" and Usertype = "staff";

DELETE from USER
where Username = "ethan_roswell" and Usertype = "staff";

