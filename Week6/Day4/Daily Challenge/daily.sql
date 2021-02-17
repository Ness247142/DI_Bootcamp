
-- Create a table orders and a table items. You decide which fields should be in each table, but each item should have a price.
-- There is a relationship of one to many between the orders and the table items
-- Create a function that returns the total price for a given order
-- Bonus :
-- Create a table users
-- There is a relationship of one to many between the table user and the table orders
-- Create a function that returns the total price for a given order of a given user


CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    FOREIGN KEY users(user_id)
)

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    item_price SMALLINT NOT NULL,
    FOREIGN KEY orders(order_id)
)



CREATE FUNCTION total_price_items
    RETURNS int AS $total_price$
    BEGIN
    	RETURN (SELECT item_price*item_id FROM items WHERE items.item_price = final_price)
    END;
    $total_price$ LANGUAGE plpgsql


SELECT * FROM total_price_items;



CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_id FOREIGN KEY orders(customer_id) REFERENCES orders(id) ON DELETE CASCADE,
)


CREATE FUNCTION total_price_user
    RETURNS int AS $total_price$
    BEGIN
    	RETURN (SELECT item_price*user_id FROM items, users WHERE items.item_price = final_price)
    END;
    $total_price$ LANGUAGE plpgsql


SELECT * FROM total_price_user;
