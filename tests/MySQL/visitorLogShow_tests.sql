SET @Visitor = 'isabella_rodriguez';
SET @ShowName ='Bald Eagle Show';
SET @DateTime1 = STR_TO_DATE('10/15/2018 2:00:00 PM','%m/%d/%Y %r');

SET @Visitor = 'isabella_rodriguez';
SET @ExhibitName = 'Birds';
SET @DateTime2 = STR_TO_DATE('10/15/2018 2:00:00 PM','%m/%d/%Y %r');

DELETE FROM VISITSHOWS Where Visitor = @Visitor and ShowName = @ShowName and DateTime = @DateTime1;
DELETE FROM VISITEXHIBIT Where Visitor = @Visitor and ExhibitName = @ExhibitName and DateTime = @DateTime2;


-- INSERT INTO VISITSHOWS (Visitor, ShowName, DateTime) VALUES ($Visitor, $ShowName, $DateTime);
-- INSERT INTO VISITEXHIBIT(Visitor, ExhibitName, DateTime) VALUES ($Visitor, $ExhibitName, $DateTime);

INSERT INTO VISITSHOWS (Visitor, ShowName, DateTime) VALUES (@Visitor , @ShowName, @DateTime);
INSERT INTO VISITEXHIBIT(Visitor, ExhibitName, DateTime) VALUES (@Visitor, @ExhibitName, @DateTime);