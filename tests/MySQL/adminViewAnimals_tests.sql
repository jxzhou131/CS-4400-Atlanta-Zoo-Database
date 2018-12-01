-- view all animals
-- if no input is specified
SELECT * 
FROM ANIMAL;


-- select  a single animal
-- all five fields must be provided

-- SELECT*
-- FROM ANIMAL
-- where Name = $Name and Species = $Species and Type = $Type and Age = $Age and Exhibit = $Exhibit
-- order by Name;

SELECT*
FROM ANIMAL
where Name ="Brad" and Species = "Bald Eagle" and Type = "Bird" and Age ="48" and Exhibit = "Birds"
order by Name;

SELECT*
FROM ANIMAL
where Name ="Goldy" and Species = "Goldfish" and Type = "Fish" and Age ="12" and Exhibit = "Pacific";

SELECT*
FROM ANIMAL
where Name ="Greg" and Species = "Goat" and Type = "Mammal" and Age ="72" and Exhibit = "Mountainous";

SELECT*
FROM ANIMAL
where Name ="Lincoln" and Species = "Lion" and Type = "Mammal" and Age ="96" and Exhibit = "Sahara";

SELECT*
FROM ANIMAL
where Name ="Nemo" and Species = "Clowfish" and Type = "Fish" and Age ="24" and Exhibit = "Pacific";

SELECT*
FROM ANIMAL
where Name ="Pedro" and Species = "Poison Dart frog" and Type = "Amphibian" and Age ="36" and Exhibit = "Jungle";

-- delete a specific animal from animal
-- must provide all the five fields

-- DELETE from ANIMAL
-- where Name = $Name and Species = $Species and Type = $Type and Age = $Age and Exhibit = $Exhibit;

DELETE from ANIMAL
where Name ="Brad" and Species = "Bald Eagle" and Type = "Bird" and Age ="48" and Exhibit = "Birds";

DELETE from ANIMAL
where Name ="Goldy" and Species = "Goldfish" and Type = "Fish" and Age ="12" and Exhibit = "Pacific";

DELETE from ANIMAL
where Name ="Greg" and Species = "Goat" and Type = "Mammal" and Age ="72" and Exhibit = "Mountainous";

DELETE from ANIMAL
where Name ="Lincoln" and Species = "Lion" and Type = "Mammal" and Age ="96" and Exhibit = "Sahara";

DELETE from ANIMAL
where Name ="Nemo" and Species = "Clowfish" and Type = "Fish" and Age ="24" and Exhibit = "Pacific";

DELETE from ANIMAL
where Name ="Pedro" and Species = "Poison Dart frog" and Type = "Amphibian" and Age ="36" and Exhibit = "Jungle";

