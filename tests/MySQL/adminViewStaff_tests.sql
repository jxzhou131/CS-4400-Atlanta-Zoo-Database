-- search for all staff
-- if no input is specified


-- select Username, Email 
-- from USER u, STAFF s
-- where u.Username = s.SUsername and u.Usertype ="staff"
-- and u.Username = $u.Username AND Email = $u.Email;
-- order by Username;

select Username, Email 
from USER u, STAFF s
where u.Username = s.SUsername and u.Usertype ="staff"
and u.Username = 'benjamin_rao' AND Email = 'benjaminrao@gmail.com'
order by Username;

-- delete a specific staff from user
-- and staff table (will automatically get deleted since foreign key cascaded)

-- DELETE from USER
-- where Username = $Username and UserType = $UserType;

DELETE from USER
where Username = "martha_johnson" and UserType = "staff";

DELETE from USER
where Username = "benjamin_rao" and UserType = "staff";

DELETE from USER
where Username = "ethan_roswell" and UserType = "staff";

