/* update the Person table. */
UPDATE Person
SET age = 27
WHERE last_name = 'Snow';

UPDATE Person
SET age = 18
WHERE first_name = 'Walter Junior';

/* delete entry from Person table. */
DELETE FROM Person
WHERE first_name = 'Walter' and last_name = 'White';

/* delete entry of person deleted in the step above from the EyesColor table. */
DELETE FROM EyesColor
WHERE person_id = (
    SELECT id FROM Person
    WHERE first_name = 'Walter' AND last_name = 'White');

/* display all the table colums with first name in ascending order. */
SELECT * FROM Person
ORDER BY first_name ASC;
