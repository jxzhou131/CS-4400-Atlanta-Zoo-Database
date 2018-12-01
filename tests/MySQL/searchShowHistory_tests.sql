-- select specific tuple
-- all the inputs are given


-- select * from
-- ((select ShowName, DateTime from VISITSHOWS
-- where Visitor = $Visitor) as vs
-- natural join
-- (select Name as ShowName, DateTime, Location as Exhibit
-- from SHOWS) as s)
-- where ShowName = $ShowName and DateTime = $DateTime and Exhibit = $Exhibit
-- order by DateTime;

select * from
((select ShowName, DateTime from VISITSHOWS
where Visitor = 'xavier_swenson') as vs
natural join
(select Name as ShowName, DateTime, Location as Exhibit
from SHOWS) as s)
where ShowName = 'Feed the Fish' and DateTime = STR_TO_DATE('10/12/18 2:00:00 PM','%m/%d/%Y %r') and Exhibit = 'Pacific'
order by DateTime;