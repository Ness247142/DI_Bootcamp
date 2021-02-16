
-- Create 3 different tables, each one with a different relationship.
-- Join them with all the types of PostgreSQL Joins



CREATE TABLE employees (
   employee_id SERIAL PRIMARY KEY,
   name VARCHAR (100) NOT NULL
);


INSERT INTO employees (name) 
VALUES ('Alex'), 
('Ali'), 
('Jacob'), 
('Anna'), 
('Saul'), 
('Kenny'), 
('Tom'), 
('Sally');



CREATE TABLE customer (
   customer_id SERIAL PRIMARY KEY,                  
   name VARCHAR (100)
);



INSERT INTO customer (name)
VALUES ('Marev'), 
('Moses'), 
('Levy'), 
('Abdul'), 
('Chris'), 
('Kate'), 
('Thomas'), 
('Samuel');



CREATE TABLE payment (
   payment_id SERIAL PRIMARY KEY,                  
   customer_id SERIAL,                 
   employee_id SERIAL, 
   amount SERIAL,
   FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
   FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
);


INSERT INTO payment(amount)                                  
VALUES (2000), 
(3000), 
(3000), 
(4000), 
(4000), 
(5000), 
(5000), 
(5000);


We want to know how much each customer has paid to which employee.
SELECT customer.name, payment.amount
FROM customer
LEFT JOIN payment 
ON payment.customer_id = customer.customer_id 
ORDER BY customer.name, payment.amount ASC;



We want to know which employee received which payment.
SELECT employees.name , payment.amount
FROM employees
RIGHT JOIN payment 
ON payment.employee_id = employees.employee_id 
ORDER BY employees.name, payment.amount ASC;



We want to know which customer payed to which employee and how much they paid them (INNER JOIN)
SELECT customer.name, employees.name, payment.amount
FROM customer 
INNER JOIN payment 
ON payment.customer_id = customer.customer_id
INNER JOIN employees 
ON payment.employee_id = employees.employee_id
ORDER BY customer.name ASC;


We want to know which customer payed to which employee (LEFT and RIGHT JOIN)
SELECT customer.name, employees.name, payment.amount
FROM customer 
LEFT JOIN payment 
ON payment.customer_id = customer.customer_id
RIGHT JOIN employees 
ON payment.employee_id = employees.employee_id
ORDER BY customer.name ASC;


We want to know which customer payed to which employee (FULL JOIN)
SELECT customer.name, employees.name, payment.amount
FROM customer 
FULL JOIN payment 
ON payment.customer_id = customer.customer_id
FULL JOIN employees 
ON payment.employee_id = employees.employee_id;
ORDER BY customer.name ASC;

