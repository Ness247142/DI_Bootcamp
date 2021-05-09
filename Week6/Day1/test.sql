
CRUD

C -> Create - keyword: Insert
R -> Retrieve - keyword: Select
U -> Update - keyword: Update
D -> Delete - keyword: Delete


How SELECT works:

SELECT <columns> FROM <table> WHERE fname ="Adam";
SELECT fname, age FROM people;
SELECT * FROM people; slect everything in the table
SELECT * FROM people WHERE age >= 25;



How INSERT works:

INSERT INTO <table> (<columns>) VALUES (<values>)

INSERT INTO people(fname, lname, age) VALUES ("Dave", "Davidson", 45)
INSERT INTO people VALUES (5, "Eli", "Elisov", 33)



How UPDATE works:

UPDATE <table> SET <column> = <value> WHERE <condition>;

UPDATE people SET fname ="Robert" WHERE id=2;
UPDATE people SET fname ="Robert" -> Every single person will be called "Robert"


How DELETE works:

DELETE FROM <table> WHERE <condition>

DELETE FROM people WHERE id > 2;
DELETE FROM people; -> delete everything in the tbale




Instead of = you can use LIKE with a wilcard "%something%"

