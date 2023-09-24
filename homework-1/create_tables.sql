-- SQL-команды для создания таблиц
CREATE TABLE employees (
	employee_id	int primary key,
	first_name varchar(15) not null,
	last_name varchar(15) not null,
	title varchar(50) not null,
	birth_date date,
	notes text
);

CREATE TABLE customers(
	customer_id varchar(10) primary key,
	company_name varchar(50) not null,
	contact_name varchar(50) not null
);

CREATE TABLE orders(
	order_id int primary key,
	customer_id varchar(5) not null,
	employee_id int,
	order_date date,
	ship_city varchar (50) not null
)