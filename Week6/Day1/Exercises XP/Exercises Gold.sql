-- Exercise Gold #2

-- Fetch all the data from the table.
-- Fetch all the students first_name and last_name.
-- For the following questions, only fetch the first_name and last_name of the students.
-- Fetch the student which id is equal to 2.
-- Fetch the student with the last_name Benichou AND the first_name Marc.
-- Fetch the students with the last_name Benichou OR the first_name Marc.
-- Check the difference between the request 2 and 3.
-- Fetch the students which first_name contains the letter a.
-- Fetch the students which first_name starts with the letter a.
-- Fetch the students which first_name ends with the letter a.
-- Fetch the students where the second to last letter of the first_name is a (Example: Leah).
-- Fetch the students which the id are 1 AND 3 

-- Fetch the students, which birth_date is equal or after the 1/01/2000. (show their first_name, last_name and birth_date)


1. SELECT * FROM students
1	"Marc"	"Benichou"	"1998-11-02"
2	"Yoan"	"Cohen"		"2010-12-03"
3	"Leah"	"Benichou"	"1987-07-27"
4	"Amelia" "Dux"		"1996-04-07"
5	"David"	"Grez"		"2003-06-14"
6	"Omer"	"Simpson"	"1980-10-03"
7      "Nessim" "Azoulay"  "1996-07-24"


2. SELECT first_name, last_name FROM students
"Marc"	"Benichou"
"Yoan"	"Cohen"
"Leah"	"Benichou"
"Amelia" "Dux"
"David"	"Grez"
"Omer"	"Simpson"
"Nessim" "Azoulay"


3.1 SELECT first_name, last_name FROM students WHERE id = 2
"Yoan"	"Cohen"


3.2 SELECT first_name, last_name FROM students 
WHERE first_name = 'Marc' AND last_name = 'Benichou'
"Marc"	"Benichou"


3.3 SELECT first_name, last_name FROM students 
WHERE first_name = 'Marc' OR last_name = 'Benichou'
"Marc"	"Benichou"
"Leah"	"Benichou"


3.4 AND fullfills both requests. OR allows us to choose between two different options.


3.5 SELECT first_name, last_name FROM students 
WHERE first_name LIKE '%a%'
"Marc"	"Benichou"
"Yoan"	"Cohen"
"Leah"	"Benichou"
"Amelia" "Dux"
"David"	"Grez"


3.6 SELECT first_name, last_name FROM students 
WHERE first_name LIKE 'A%'
"Amelia" "Dux"


3.7 SELECT first_name, last_name FROM students 
WHERE first_name LIKE '%a'
"Leah"	"Benichou"
"Amelia" "Dux"


3.8 SELECT first_name, last_name FROM students 
WHERE first_name LIKE '%a_'
"Yoan"	"Cohen"
"Leah"	"Benichou"


3.9 SELECT first_name, last_name FROM students 
WHERE id = 1 OR id = 3
"Marc"	"Benichou"
"Leah"	"Benichou"


4. SELECT first_name, last_name, birth_date FROM students 
WHERE birth_date >= '01/01/2000'
"Yoan"	"Cohen"	"2010-12-03"
"David"	"Grez"	"2003-06-14"
