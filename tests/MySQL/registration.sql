-- STEP 1 email and username must be unique
-- check whether the email or username has been used

select * from USER
where Email = 'xavierswenson@outlook.com' or Username = 'xavier_swenson';

select * from USER
where Email = 'xavierswenson@outlook.com' or Username = 'isabella_rodriguez';

-- STEP 2 if does not exist and the password matches the confirmedPassword
-- continue with registration

-- insert into USER
-- values 
-- ('robert_bernheardt', md5('password7'), 'robertbernheardt@yahoo.com', 'visitor')

-- STEP 3 
-- 1) if register as Visitor

-- insert into VISITOR
-- ('robert_bernheardt')

-- 2) if register as Staff

-- insert into STAFF
-- ('robert_bernheardt')