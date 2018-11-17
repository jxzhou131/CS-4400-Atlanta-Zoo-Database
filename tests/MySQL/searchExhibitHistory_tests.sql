-- searchExhibitHistory

-- search for all records
-- when there are no inputs, range == no input if min > max
select * from 
((select ExhibitName, DateTime 
from VISITEXHIBIT as v2
where Visitor = 'robert_bernheardt') as visitExhibit1
Natural Join
(select ExhibitName, count(*) as numVisits 
from VISITEXHIBIT as v1
where Visitor = 'robert_bernheardt'
group by ExhibitName
order by numVisits) as visitExhibit2)
order by numVisits DESC;

-- search for specific range of number of visits
-- if specified range of numVisits only , min <= max
select * from 
((select ExhibitName, DateTime 
from VISITEXHIBIT as v2
where Visitor = 'robert_bernheardt') as visitExhibit1
Natural Join
(select ExhibitName, count(*) as numVisits 
from VISITEXHIBIT as v1
where Visitor = 'robert_bernheardt'
group by ExhibitName
order by numVisits) as visitExhibit2)
where numVisits between 1 and 3
order by numVisits DESC;

-- search for records on a specific datetime
-- if specify datetime only
select * from 
((select ExhibitName, DateTime 
from VISITEXHIBIT as v2
where Visitor = 'robert_bernheardt') as visitExhibit1
Natural Join
(select ExhibitName, count(*) as numVisits 
from VISITEXHIBIT as v1
where Visitor = 'robert_bernheardt'
group by ExhibitName
order by numVisits) as visitExhibit2)
where DateTime = str_to_date('5/8/2017 1:00:00 PM','%m/%d/%Y %r')
order by numVisits DESC;

-- search for records on a specific exhibit
-- if specify exhibit name only
select * from 
((select ExhibitName, DateTime 
from VISITEXHIBIT as v2
where Visitor = 'robert_bernheardt') as visitExhibit1
Natural Join
(select ExhibitName, count(*) as numVisits 
from VISITEXHIBIT as v1
where Visitor = 'robert_bernheardt'
group by ExhibitName
order by numVisits) as visitExhibit2)
where numVisits between 1 and 3
and DateTime = str_to_date('5/8/2017 1:00:00 PM','%m/%d/%Y %r')
order by numVisits DESC;

-- search for specific entries
-- all variables are specified
select * from 
((select ExhibitName, DateTime 
from VISITEXHIBIT as v2
where Visitor = 'robert_bernheardt') as visitExhibit1
Natural Join
(select ExhibitName, count(*) as numVisits 
from VISITEXHIBIT as v1
where Visitor = 'robert_bernheardt'
group by ExhibitName
order by numVisits) as visitExhibit2)
where numVisits between 1 and 3
and DateTime = str_to_date('5/8/2017 1:00:00 PM','%m/%d/%Y %r')
and ExhibitName = 'Sahara'
order by numVisits DESC;