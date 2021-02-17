
Basic Select Statement

Write a query to display the names (first_name, last_name) using an alias name “First Name”, “Last Name” from employee table.
SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees

Write a query to get a unique department ID from employee table.
SELECT DISTINCT department_id FROM employees

Write a query to get the details of all employees from the employee table in descending order by their first name.
SELECT * FROM employees ORDER BY first_name DESC


Write a query to get the names (first_name, last_name), salary and 15% of salary as PF (ie. alias) for all the employees.
SELECT first_name, last_name, salary, salary*0.15 as PF FROM employees

Write a query to get the employee ID, names (first_name, last_name) and salary in ascending order according to their salary.
SELECT employee_id, first_name, last_name, salary FROM employees ORDER BY salary ASC

Write a query to get the total salaries paid to the employees.
SELECT SUM(salary) FROM employees

Write a query to get the maximum and minimum salary paid to the employees.
SELECT MAX(salary), MIN(salary) FROM employees

Write a query to get the average salary paid to the employees.
SELECT AVG(salary) FROM employees

Write a query to get the number of employees working in the company.
SELECT COUNT(*) FROM employees

Write a query to get all the first name from the employees table in upper case.
SELECT UPPER(first_name) FROM employees

Write a query to get the first three characters of the first name for all the employees in the employees table.
SELECT SUBSTRING(first_name, 1, 3) FROM employees

Write a query to get the full name of all the employees from employees table. You have to include the first name and last name
SELECT CONCAT(first_name,' ', last_name) FROM employees

Write a query to get the first name, last name and the length of the full name of all the employees from employees table.
SELECT first_name, last_name, LENGTH(first_name) + LENGTH(last_name) FROM employees

Write a query to check whether the first_name column of the employees table containing any number.
SELECT * FROM employees WHERE first_name ~* '[0-9]'

Write a query to select first ten records from a table.
SELECT employee_id, first_name, last_name FROM employees LIMIT 10;



Restricting And Sorting

Write a query to display the name, including first_name and last_name and salary for all employees whose salary is between $10,000 and $15,000.
SELECT first_name, last_name, salary FROM employees WHERE salary between 10000 and 15000


Write a query to display the name, including first_name and last_name and hire date for all employees who were hired in 1987.
SELECT first_name, last_name, hire_date FROM employees WHERE hire_date LIKE '%1987%'


Write a query to get the first name of the employees who holds the letter ‘c’ and ‘e’ in the first name.
SELECT first_name FROM employees WHERE first_name LIKE '%c%' and first_name LIKE '%e%'


Write a query to display the last name, job, and salary for all the employees who don’t work as a Programmer or a Shipping Clerk, and not drawing the salary $4,500, $10,000, or $15,000.
SELECT last_name, job_id, salary FROM employees WHERE job_id NOT IN(9, 17) AND salary NOT IN(4500, 10000, 15000) 


Write a query to display the last names of employees whose last name contain exactly six characters.
SELECT last_name FROM employees WHERE last_name LIKE '______'


Write a query to display the last name of employees having ‘e’ as the third character.
SELECT last_name FROM employees WHERE last_name LIKE '__e'


Write a query to display the jobs/designations available in the employees table.
SELECT DISTINCT job_id FROM employees

Write a query to select all information of employees whose last name is either ‘JONES’ or ‘BLAKE’ or ‘SCOTT’ or ‘KING’ or ‘FORD’.
SELECT * FROM employees WHERE last_name IN('Jones', 'Blake', 'Scott', 'King', 'Ford')



Update Statement

Write a SQL statement to change the email and commission_pct column of the employees table with ‘not available’ and 0.10 for all employees for those employees whose department_id is 110.
UPDATE employees SET email= 'not available' WHERE department_id = 110

Write a SQL statement to change the email column of the employees table with ‘available’ for those employees who belongs to the ‘Accounting’ department.
UPDATE employees SET email='available' WHERE department_id=(SELECT department_id FROM departments WHERE department_name='Accounting')

Write a SQL statement to change the salary of an employee to 8000 whose ID is 105, if the existing salary is less than 5000.
UPDATE employees SET salary= 8000 WHERE employee_id=105 AND salary < 5000

Write a SQL statement to increase the salary of employees under the department 40, 90 and 110 according to the company rules that, the salary will be increased by 25% of the department 40, 15% for department 90 and 10% of the department 110 and the rest of the department will remain same.
UPDATE employees SET salary= CASE department_id 
WHEN 40 THEN salary+(salary*.25) 
WHEN 90 THEN salary+(salary*.15)
WHEN 110 THEN salary+(salary*.10)
ELSE salary
END
WHERE department_id IN (40,50,50,60,70,80,90,110)
