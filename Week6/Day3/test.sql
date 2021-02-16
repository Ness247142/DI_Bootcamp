
Table Relationships
ONE-TO-MANY
ONE-TO-ONE
MANY-TO-MANY

SELECT person.name, person.surname, foods.name 
FROM person 
LEFT JOIN person_foods
ON person_id = person_foods.person_id
LEFT JOIN foods 
ON person_foods.food_id = foods.id
ORDER BY person.surname ASC;