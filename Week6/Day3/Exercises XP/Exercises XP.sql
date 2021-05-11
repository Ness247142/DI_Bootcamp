
-- #Exercise 1: Dvd Rental

-- Get a list of all film languages
SELECT name FROM language

-- Get a list of all films joined with their languages – select only the film title, description, and language name. Try your query with different joins:

-- Get all films, even if they don’t have languages
-- Get all languages, even if there are no films in those languages. Which languages are these?

SELECT title, description, language FROM film
INNER JOIN language
ON film.language_id = language.language_id


SELECT title, description, language FROM film
FULL JOIN language
ON film.language_id = language.language_id


-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR (100) NOT NULL,
)

INSERT INTO new_film(name)
VALUES ("Honest Thief"),
("Country at Heart"),
("Little Big Women"),
("2 Hearts"),
("Chick Fight");

-- Create a new table called customer_review, to contain data about film reviews that customers will make.

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER FOREIGN KEY language(language_id),
    title VARCHAR (100),
    score SMALLINT,
    review_text TEXT,
    last_update DATE
)

-- Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review
-- score – the rating of the review (1-10)
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.


-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update) VALUES(1, 1, 'Review 1', 8, 'A great movie to enjoy at home!', '2021-02-16')

INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update) VALUES(2, 1, 'Review 2', 3, 'A terrible movie with a terrible storytelling!', '2021-02-16' )


-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE id=3

Once we deleted the movie, the entire review was deleted as well





-- # Exercise 2 : Dvd Rental

-- Use UPDATE to change the language of some films. Make sure that you use valid languages…

UPDATE language SET name='Spanish' WHERE language_id=3

UPDATE language SET name='Hindi' WHERE language_id=4


-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
The references defined for the customer table are store_id and address_id.
The numbers are chosen according to the reference id, so the whole table can be in a random order depending on the input


-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review
It does not need need an extra checking because the references are on a foreign key.


-- Find out how many rentals are still outstanding. (ie. have not been returned to the store yet)
SELECT count(*) FROM rental WHERE return_date is NULL


-- Mark the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT rental.rental_id, film.title, film.rental_rate
FROM inventory 
JOIN rental 
ON inventory.inventory_id = rental.inventory_id
JOIN film 
ON film.film_id = inventory.film_id
WHERE return_date is NULL
ORDER BY rental_rate DESC
LIMIT 30


-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he is talking about?

-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
-- The 4th film : His friend Matthew Mahan watched this film, too. It had the word ‘boat’ in the title or description, and it looked like it was a very expensive DVD to replace.


select film.title
from (actor join film_actor on actor.actor_id = film_actor.actor_id)
join film on film.film_id = film_actor.film_id
where film.description like '%Sumo%' 
and actor.first_name = 'Penelope' 
and actor.last_name = 'Monroe'

SELECT film.title
FROM (category JOIN film_category ON category.category_id = film_category.category_id)
JOIN film ON film.film_id = film_category.film_id
WHERE film.length < 60
AND film.rating = 'R'
AND category.category_id = 6

SELECT film.title, customer.first_name, customer.last_name,
payment.payment_id, payment.amount, return_date
FROM rental JOIN customer
ON rental.customer_id = customer.customer_id
JOIN payment ON rental.rental_id = payment.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE customer.first_name = 'Matthew'
AND customer.last_name = 'Mahan'
AND rental.return_date < '2005-08-01'
AND rental.return_date > '2005-07-28'
AND payment.amount > 4;

SELECT film.title, film.description, film.replacement_cost
FROM film
JOIN inventory
ON film.film_id = inventory.film_id
JOIN rental
ON rental.inventory_id = inventory.inventory_id
JOIN customer
ON rental.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew'
AND customer.last_name = 'Mahan'
AND film.title LIKE '%boat%' 
OR film.description LIKE '%boat%'
ORDER BY film.replacement_cost DESC
LIMIT 1
