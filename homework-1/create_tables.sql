-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customer_id text PRIMARY KEY,
	company_name text,
	contact_name text
);

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name text,
	last_text text,
	title text,
	birth_date text,
	notes text
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id text REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date text,
	ship_city text
);

SELECT * FROM customers
SELECT * FROM employees
SELECT * FROM orders
