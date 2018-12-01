
-- search for all staff
-- if no input is specified

-- select Username, Email 
-- from USER u, VISITOR s
-- where u.Username = s.VUsername and u.UserType ="visitor"
-- and u.Email = $u.Email
-- and u.Username = $u.Username
-- order by $Attribute $ASC/DSC;

select Username, Email 
from USER u, VISITOR s
where u.Username = s.VUsername and u.UserType ="visitor"
and u.Email = "xavierswenson@outlook.com"
and u.Username = "xavier_swenson"
order by Username ASC;


-- delete a specific visitor from user
-- and visitors table (will automatically get deleted since foreign key cascaded)

-- DELETE from USER
-- where Username = $Username and UserType = $UserType;

DELETE from USER
where Username = "xavier_swenson" and UserType = "visitor";

DELETE from USER
where Username = "isabella_rodriguez" and UserType = "visitor";

DELETE from USER
where Username = "nadias_tevens" and UserType = "visitor";

DELETE from USER
where Username = "robert_bernheardt" and UserType = "visitor";