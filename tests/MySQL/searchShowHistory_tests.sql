select * from
(select ShowName, DateTime from VISITSHOWS
where Visitor = 'xavier_swenson') as vs
natural join
(select Name as ShowName, DateTime, Location as Exhibit
from SHOWS) as s;