-- Exercises 1

-- Use SQL to get the following from the database:

-- All items, ordered by price (lowest to highest).
SELECT * FROM items ORDER BY item_price;

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
SELECT * FROM items WHERE item_price > 80 ORDER BY item_price DESC;

-- The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
SELECT first_name, last_name FROM customers ORDER BY first_name ASC LIMIT 3;

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT last_name FROM customers ORDER BY last_name DESC;




-- Create a table named purchases. It should have 2 columns : customer_id and item_id. These columns are references from the tables customers and items. Edit the data of the purchases table:
-- Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
-- Add 5 rows which reference existing customers and items.

CREATE TABLE purchases
(
    purchase_id SERIAL PRIMARY KEY,
    customer_id VARCHAR(100) NOT NULL,
    item_id VARCHAR(100) NOT NULL
)


-- Use SQL to get the following from the database:


-- All purchases. Is this information useful to us?
SELECT * FROM purchases
-- NO. It's not useful to us, because there is no data about the customers and the items' price


-- All purchases, joining with the customers table.
SELECT * FROM purchases JOIN customers ON purchases.customer_id = customers.customer_id;


-- Purchases of the customer with the ID equal to 4.
SELECT * FROM purchases JOIN customers ON purchases.customer_id = customer_id WHERE customer_id=4


-- Purchases for a large desk AND a small desk
SELECT * FROM purchases JOIN items ON purchases.item_id = items.id WHERE item_name='Small Desk' AND item_name='Large Desk'



-- Create a purchase for Scott Scott – he bought a hard drive.
-- Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
-- Customer first name
-- Customer last name
-- Item name

INSERT INTO items (item_name, item_price) VALUES ('Hard Drive', 400)

INSERT INTO customers (first_name, last_name) VALUES ('Scott', 'Scott')

INSERT INTO purchases (customer_id, item_id) VALUES (3, 4)

SELECT * FROM purchases JOIN customers ON purchases.customer_id = customers.id JOIN items ON purchases.item_id = items.id

SELECT first_name, last_name, item_name FROM purchases JOIN customers ON purchases.customer_id = customers.id JOIN items ON purchases.item_id = items.id




-- Exercises 2
-- We will use the newly installed dvdrental database.


-- Write a query to select all the columns from the table “customer” in the database named dvdrental.
SELECT * FROM customer


-- Write a query to display the names (first_name, last_name) using an alias named “full_name”.
SELECT first_name, last_name AS full_name FROM customer


-- You want to know every date where one or several accounts were created. Write a query to select the dates of creation from the “customer” table, it shouldn’t have duplicates.
SELECT DISTINCT create_date FROM customer


-- Write a query to get the details of all customers from the customer table in descending order by their first name.
SELECT * FROM customer ORDER BY first_name DESC


-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC


-- Write a query to get the address, the district and the phone number from the customers living in the district Texas in the “address” table.
SELECT address, district, phone FROM address WHERE district = 'Texas'


-- Write a query to retrieve the details of the movies with the id 15 and 150.
SELECT * FROM film WHERE film_id IN (15, 150)


-- Pick your favorite movie. Write a query to see if the rental shop owns it. Write a query to get the film ID, the title, the description, the length and the rental rate from the film table for your movie title.
SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'The Round Up'


-- Didn’t find it ? Maybe you made a mistake in the name. Write a query to get the film ID, the title, the description, the length and the rental rate from the “film” table for all the movies starting with the two first letters of your movie.
SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'Ro%'


-- You want to have a choice between ten propositions of movies and you want the cheapest ones. Write a query to find the 10th cheapest movies.
SELECT title FROM film ORDER BY rental_rate LIMIT 10


-- You are not satisfied with the results. Write a query to find the 10th next cheapest movies. 
SELECT title FROM film ORDER BY rental_rate OFFSET 10 FETCH FIRST 10 ROWS ONLY 


-- Write a query to join the data of the customer table and the payment table. You want to get the amount and the date of every payment made by a customer, ordered by his id (from 1 to…).
SELECT amount, payment_date FROM customer INNER JOIN payment ON customer.customer_id = payment.customer_id ORDER BY customer.customer_id


-- You need to check your inventory. Write a query to get all the movies which are not in the inventory.
SELECT * FROM film INNER JOIN inventory ON film.film_id = inventory.film_id WHERE film.film_id NOT IN (inventory.film_id)


-- Write a query to find which city is in which country.
SELECT city, country FROM city INNER JOIN country ON country.country_id = country.country_id





