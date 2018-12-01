-- admin add shows

-- INSERT INTO SHOWS (Name, DateTime, Host, Location)
-- VALUES ($Name, $DateTime, $Host, $Location);

-- first find if there exist tuple that has the same datetime and host
SELECT DateTime, Host From SHOWS
WHERE DateTime = STR_TO_DATE($DateTime , '%m/%d/%Y %r') AND Host = $Host;

INSERT INTO SHOWS (Name, DateTime, Host, Location)
VALUES ("abc", STR_TO_DATE('06/01/2000 12:00:00 AM', '%m/%d/%Y %r'), "martha_johnson", "Pacific");