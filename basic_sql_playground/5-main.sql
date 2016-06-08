/* join two tables to get all distinct lastnames for a show.*/
SELECT DISTINCT last_name FROM Person
    JOIN TVShowPerson ON TVShowPerson.person_id = Person.id,
         TVShow ON TVShowPerson.tvshow_id = TVShow.id
    WHERE name = "Game of Thrones" ORDER BY last_name ASC;

/* count the number of people under 30 */
SELECT COUNT(age) FROM Person WHERE age > 30;

/* create an all people record with id, full name, age, eye color and tv show listed.*/
SELECT Person.id, first_name, last_name, age, color, name FROM Person
    JOIN TVShowPerson ON TVShowPerson.person_id = Person.id,
         TVShow ON TVShow.id = TVShowPerson.tvshow_id,
         EyesColor ON EyesColor.person_id = Person.id;

/* show the sum of all the ages in the Person table. */
SELECT SUM(age) FROM Person;
