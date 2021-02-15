-- #Exercise 1: DVD Rental



-- Find out how many films there are for each rating
1. SELECT count(rating) FROM film WHERE rating = 'G'
SELECT count(rating) FROM film WHERE rating = 'PG'
SELECT count(rating) FROM film WHERE rating = 'PG-13'
SELECT count(rating) FROM film WHERE rating = 'R'
SELECT count(rating) FROM film WHERE rating = 'NC-17'



-- Get a list of all the movies that have a rating of G or PG-13
2. SELECT title, rating FROM film WHERE rating IN('G', 'PG-13')

-- Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
SELECT title, rating FROM film WHERE rating IN('G', 'PG-13') AND length = 120 AND rental_rate < 3 ORDER BY title ASC


-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
3. UPDATE customer SET first_name = 'Nessim', last_name = 'Azoulay', email = 'ness.azoulay.ta@gmail.com' WHERE customer id= 3


-- Now find the customer’s address, and use UPDATE to change it to an address of your own (or make one up).
4. SELECT * FROM customer JOIN address on customer.address_id = address.address_id ORDER BY customer_id
UPDATE address SET address = 'Heart Street' WHERE address_id = 3






-- # Exercise 2

UPDATE:
1. UPDATE students SET birth_date = '1998-11-02' WHERE last_name = 'Benichou'

2. UPDATE students SET last_name = 'Guez' WHERE last_name = 'Grez'


DELETE:
1. DELETE FROM students WHERE id=3


COUNT:
1. SELECT count(*) FROM students

2. SELECT count(*) FROM students WHERE birth_date > '2000-01-01'



INSERT/ALTER:
1. ALTER TABLE students ADD column math_grade SMALLINT

2. INSERT INTO students(math_grade) VALUES (80) WHERE id=1

3. INSERT INTO students(math_grade) VALUES (90) WHERE id=2 and id=4

4. INSERT INTO students(math_grade) VALUES (40) WHERE id=6

5. SELECT count(*) FROM students WHERE math_grade > 83

6. INSERT INTO students(first_name, last_name, birth_date) VALUES('Omer', 'Simpson', '1980-10-03')

INSERT INTO students(math_grade) VALUES (70) WHERE id=8

7. SELECT first_name, last_name, math_grade AS total_grade FROM students


SUM 
SELECT sum(math_grade) FROM students







