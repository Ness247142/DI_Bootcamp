

HAVING is like WHERE but after GROUP BY


CSV
COMMA SEPERATED VALUES

Simplified form of rows and columns
Very useful for importing large amounts of data

ama,admson,22,1
bob, benson, 35,2
charlie,chaplin,34,16

COPY actors(first_name, last_name, age, number_oscars)
FROM 'Absolute PATH to file'
DELIMETER ','
CSV;




  OBJECT         RELATIONAL       MAPPER ORM
classes / OOP   tables etc     link between them



SELECT * FROM actors WHERE name = 'Tom'
actors.filter(name='Tom')


ORM: 
class actor:
first_name = string(50)
last_name = string(50)
age = integer

WE can write Python code within ORM




TRANSACTIONS
BEGIN
	UPDATE account SET balance = balance - 100 WHERE user_id = 1;
	UPDATE account SET balance = balance + 100 WHERE user_id = 2;
COMMIT



DRY - Don't repeat yourself

S - Single responsibility principle
O - Open/closed principle 
L - Liskov substitution principle
I - Interface segregation principle 
D - Dependency inversion principle -

A - Atomicity
C - Consistency
I - Isolation
D - Durability




