-- search for all shows
-- if no input is specified
select Name, Location as Exhibit, DateTime 
from SHOWS ;

-- search for show with specific name
-- if only specify the show name
select Name, Location as Exhibit, DateTime 
from SHOWS 
where Name = 'Feed the fish';

-- search for show with specific exhibit
-- if specify only the exhibit name
select Name, Location as Exhibit, DateTime 
from SHOWS 
where location = 'Pacific';

-- search for show with specific date
-- if specify only the datetime
select Name, Location as Exhibit, DateTime 
from SHOWS 
where DateTime = str_to_date('10/8/2018 12:00:00 PM','%m/%d/%Y %r');

-- search for the specific show
-- all the variables have been specified
select Name, Location as Exhibit, DateTime 
from SHOWS 
where DateTime = str_to_date('10/8/2018 12:00:00 PM','%m/%d/%Y %r') and 
Name = 'Feed the fish' and location = 'Pacific';
