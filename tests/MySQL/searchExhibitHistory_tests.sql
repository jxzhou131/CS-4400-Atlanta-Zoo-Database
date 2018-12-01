-- searchExhibitHistory

-- search for specific entries
-- all variables are specified

-- select * from 
-- ((select ExhibitName, DateTime 
-- from VISITEXHIBIT as v1
-- where Visitor = $Visitor) as visitExhibit1
-- Natural Join
-- (select ExhibitName, count(*) as numVisits 
-- from VISITEXHIBIT as v2
-- where Visitor = $Visitor
-- group by ExhibitName
-- order by numVisits) as visitExhibit2)
-- where numVisits between $minNumVisits and $maxNumVisits
-- and DateTime = $DateTime
-- and ExhibitName = $Exhibit
-- order by numVisits DESC;


select * from 
((select ExhibitName, DateTime 
from VISITEXHIBIT as v1
where Visitor = 'robert_bernheardt') as visitExhibit1
Natural Join
(select ExhibitName, count(*) as numVisits 
from VISITEXHIBIT as v2
where Visitor = 'robert_bernheardt'
group by ExhibitName
order by numVisits) as visitExhibit2)
where numVisits between 1 and 3
and DateTime = str_to_date('5/8/2017 1:00:00 PM','%m/%d/%Y %r')
and ExhibitName = 'Sahara'
order by numVisits DESC;