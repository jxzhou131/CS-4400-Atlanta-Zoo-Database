-- SET @location = 'Pacific';

-- Set @datetime = str_to_date('10/8/2018 12:00:00 PM','%m/%d/%Y %r');

-- Set @Name = 'Feed the fish';

-- -- search for the specific show
-- -- all the variables have been specified
-- select Name, Location as Exhibit, DateTime 
-- from SHOWS 
-- where DateTime = @datetime and 
-- Name = @Name and location = @location
-- order by DateTime;

-- search for the specific show
-- all the variables have been specified

-- select Name, Location as Exhibit, DateTime 
-- from SHOWS 
-- where DateTime = $DateTime and 
-- Name = $Name and location = $location
-- order by DateTime;
select Name, Location as Exhibit, DateTime
from SHOWS 
where DateTime = str_to_date('10/8/2018 12:00:00 PM','%m/%d/%Y %r') and 
Name = 'Feed the fish' and location = 'Pacific'
order by DateTime;