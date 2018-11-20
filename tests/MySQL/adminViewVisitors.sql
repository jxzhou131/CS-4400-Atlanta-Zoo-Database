-- search for all staff
-- if no input is specified
select Username, Email 
from user u, visitor s
where u.Username = s.VUsername and u.Usertype ="visitor";


-- delete a specific visitor from user
-- and visitors table (will automatically get deleted since foreign key cascaded)
DELETE from user
where Username = "xavier_swenson" and Usertype = "visitor";

DELETE from user
where Username = "isabella_rodriguez" and Usertype = "visitor";

DELETE from user
where Username = "nadias_tevens" and Usertype = "visitor";

DELETE from user
where Username = "robert_bernheardt" and Usertype = "visitor";

