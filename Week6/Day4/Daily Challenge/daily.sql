
-- Create a table orders and a table items. You decide which fields should be in each table, but each item should have a price.
-- There is a relationship of one to many between the orders and the table items
-- Create a function that returns the total price for a given order
-- Bonus :
-- Create a table users
-- There is a relationship of one to many between the table user and the table orders
-- Create a function that returns the total price for a given order of a given user


CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    full_price INTEGER
)

INSERT INTO orders(id) VALUES (1),
(2),
(3)


CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    item_price INTEGER NOT NULL
)

INSERT INTO items(item_name, item_price) 
VALUES ('Hamburger', 20), 
('Beef Steak', 35),
('French Fries', 8),
('Greek Salad', 15),
('Soda', 5)


CREATE TABLE order_to_manage(
	orders integer references orders(id) ON DELETE CASCADE,
	items integer references items(id) ON DELETE CASCADE
	)

INSERT INTO order_to_manage(orders,items) 
VALUES (1,1), 
(1,2), 
(1,4), 
(2,5), 
(2,2), 
(3,1), 
(3,3), 
(3,4), 
(3,5)

SELECT * FROM order_to_manage


CREATE FUNCTION total_price (ord INTEGER)
    RETURNS INTEGER AS $total_price$
    BEGIN
    	RETURN (SELECT sum(item_price) FROM items FULL JOIN order_to_manage ON items.id = order_to_manage.items WHERE orders= ord);
    END;
    $total_price$ LANGUAGE plpgsql


SELECT * FROM total_price(1);
SELECT * FROM total_price(2);
SELECT * FROM total_price(3);
