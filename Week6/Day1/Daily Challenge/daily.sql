
-- Using the table actors from the lesson, 
-- 1. Count how many actors are in the table
-- 2. Try to add a new actor, with some blank fields. What happens ?


1. SELECT COUNT(*) FROM actors

2

2. INSERT INTO actors(first_name, last_name, age, number_oscars)
VALUES('Tom', 'Hanks', 5)

ERROR:  INSERT has more target columns than expressions
LINE 2: (first_name, last_name, age, number_oscars)
                                ^
SQL state: 42601
Character: 44

-> When I start the query, the message answers me that there is a missing argument at 'age' because we already defined during the creation of the table 'actors', that this field cannot be NULL.


INSERT INTO actors(first_name, last_name, age, number_oscars)
VALUES('Tom', 'Hanks', '1956-07-09', 5)

1	"Matt"	    "Damon"	    "1970-08-10"	5
2	"George"    "Clooney"	  "1961-06-05"	       2
3	"Tom"	      "Hanks"	    "1956-07-09"	5
