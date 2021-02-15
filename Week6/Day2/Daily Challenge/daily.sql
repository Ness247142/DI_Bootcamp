

In this puzzle you have to go through all the SQL queries and provide us the output of the requests before executing them.
Then, execute them to make sure you were right

CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)
-- Create a new table called 'FirstTab' with 2 columns: id (as an integer) and name (10 characters max)


INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')
-- Insert new values into the 2 columns of the table 'FirstTab'


SELECT * FROM FirstTab
-- Fetch all the data from the table 'FirstTab'


CREATE TABLE SecondTab (
    id integer 
)
-- Create a new table called 'SecondTab' with 1 column: id (as an integer)


INSERT INTO SecondTab VALUES
(5),
(NULL)
-- Insert new values into the table 'SecondTab'


SELECT * FROM SecondTab
-- Fetch all the data from the table 'SecondTab'


Q1. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab a WHERE a.Id NOT IN (SELECT Id FROM SecondTab WHERE Id IS NULL )

-- Output will be 3. The id of NULL in 'FirstTab' and 'SecondTab' is taken out. We will get the id of 5, 6 and 7.


Q2. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab a WHERE a.Id NOT IN ( SELECT Id FROM SecondTab WHERE Id = 5 )

-- Output will be 3. We will get the id of 6, 7 and NULL


Q3. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab a WHERE a.Id NOT IN ( SELECT Id FROM SecondTab)

-- Output will be 2. The id of 5 and NULL from 'secondtab' are taken out


Q4. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab a WHERE a.Id NOT IN ( SELECT Id FROM SecondTab WHERE Id IS NOT NULL )

-- Output will be 3. We will get the id of 6, 7 and NULL

