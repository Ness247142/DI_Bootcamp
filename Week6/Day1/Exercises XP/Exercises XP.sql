-- Exercise XP #1

-- Use SQL to get the following data from the database:
-- All the items
-- All the items with a price above 80 (80 not included)
-- All the items with a price below 300
-- All the customers with the last name ‘Smith’ (Will you get a result ?)
-- All the customers with the last name ‘Jones’
-- All the customers with a first name that is not ‘Scott’


SELECT * FROM items
1	"Small Desk"	100
2	"Large Desk"	300
3	"Fan"		 80



SELECT * FROM items WHERE price > 80
1	"Small Desk"	100
2	"Large Desk"	300



SELECT * FROM items WHERE price < 300
1	"Small Desk"	100
3	"Fan"		80



SELECT * FROM customers WHERE last_name = 'Smith' -- No. There is no result from this query

SELECT * FROM customers WHERE last_name = 'Jones'
1	"Greg"		"Jones"
2	"Sandra"	"Jones"



SELECT * FROM customers WHERE first_name NOT LIKE 'Scott'
1	"Greg"		"Jones"
2	"Sandra"	"Jones"
4	"Trevor"	"Green"
5	"Melanie"	"Johnson"
