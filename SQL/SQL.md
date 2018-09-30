
# Table of Contents
- [1. SQL Overview](#1-sql-overview)
  * [1.1 What is SQL](#11-what-is-sql)
  * [1.2 RDBMS](#12-rdbms)
  * [1.3 Table](#13-table)
  * [1.4 Record/Row](#14-record-row)
  * [1.5 Column](#15-column)
- [2. Select](#2-select)
  * [2.1 SELECT DISTINCT](#21-select-distinct)
- [3. Where](#3-where)
  * [3.1 Operators](#31-operators)
- [4. And, Or, Not](#4-and--or--not)
  * [4.1 And](#41-and)
  * [4.2 Or](#42-or)
  * [4.3 Not](#43-not)
  * [4.4 Combining AND, OR and NOT](#44-combining-and--or-and-not)
- [5. ORDER BY](#5-order-by)
- [6. INSERT INTO](#6-insert-into)
- [7. NULL Values](#7-null-values)
- [8. UPDATE](#8-update)
- [9. DELETE](#9-delete)
- [10. LIMIT](#10-limit)
- [11. MIN/MAX](#11-min-max)
  * [11.1 MIN](#111-min)
  * [11.2 MAX](#112-max)
- [12. COUNT/AVG/SUM](#12-count-avg-sum)
  * [12.1 COUNT](#121-count)
  * [12.2 AVG](#122-avg)
  * [12.3 SUM](#123-sum)
- [13. Like](#13-like)
- [14. IN](#14-in)
- [15. BETWEEN](#15-between)
- [16. Aliases](#16-aliases)
- [17. Inner Join](#17-inner-join)
- [18. LEFT JOIN](#18-left-join)
- [19. RIGHT JOIN](#19-right-join)
- [20. SELF JOIN](#20-self-join)
- [21. GROUP BY](#21-group-by)
- [22. Having](#22-having)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# 1. SQL Overview
## 1.1 What is SQL
* SQL stands for Structured Query Language
* SQL lets you access and manipulate databases

## 1.2 RDBMS
RDBMS stands for Relational Database Management System. RDBMS is the basis for SQL, and for all modern database systems such as MS SQL Server, MySQL.

## 1.3 Table
The data in RDBMS is stored in database objects called tables. A table is a collection of related data entries and it consists of columns and rows. 

## 1.4 Record/Row
A record, also called a row, is each individual entry that exists in a table. For example, there are 91 records in the above Customers table. A record is a horizontal entity in a table.

## 1.5 Column
A column is a vertical entity in a table that contains all information associated with a specific field in a table.

# 2. Select
The SELECT statement is used to select data from a database. The data returned is stored in a result table, called the result-set.

```SQL
SELECT column1, column2, ... FROM table_name;
```

Here, column1, column2, ... are the field names of the table you want to select data from. If you want to select all the fields available in the table, use the following syntax:

```SQL
SELECT * FROM table_name;
```

```SQL
SELECT CustomerName, City FROM Customers;
```

## 2.1 SELECT DISTINCT
The SELECT DISTINCT statement is used to return only distinct (different) values. Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.

```SQL
SELECT DISTINCT Country FROM Customers;
SELECT COUNT(DISTINCT Country) FROM Customers;
```

You **cannot** do this:
```SQL
/* Wrong */
SELECT Name, DISTINCT Country FROM Customers;
```

# 3. Where
```SQL
SELECT * FROM Customers WHERE Country='Mexico';
SELECT * FROM Customers WHERE CustomerID=1;
```

## 3.1 Operators
| = | Equal |
| --- | --- |
| <> | Not equal |
| >	| Greater than |
| <	| Less than |
| >= | Greater than or equal |
| BETWEEN | Between an inclusive range |
| LIKE | Search for a pattern |
| IN | To specify multiple possible values for a column |

# 4. And, Or, Not
The WHERE clause can be combined with AND, OR, and NOT operators.

## 4.1 And
The AND operator displays a record if all the conditions separated by AND is TRUE.
```SQL
SELECT * FROM Customers WHERE Country='Germany' AND City='Berlin';
```

## 4.2 Or
The OR operator displays a record if any of the conditions separated by OR is TRUE.
```SQL
SELECT * FROM Customers WHERE City='Berlin' OR City='München';
```

## 4.3 Not
The NOT operator displays a record if the condition(s) is NOT TRUE.
```SQL
SELECT * FROM Customers WHERE NOT Country='Germany';
```

## 4.4 Combining AND, OR and NOT
You can also combine the AND, OR and NOT operators.
```SQL
SELECT * FROM Customers WHERE Country='Germany' AND (City='Berlin' OR City='München');
SELECT * FROM Customers WHERE NOT Country='Germany' AND NOT Country='USA';
```

# 5. ORDER BY
The ORDER BY keyword is used to sort the result-set in ascending or descending order.

The ORDER BY keyword sorts the records in ascending (ASC) order by default. To sort the records in descending order, use the DESC keyword.

```SQL
SELECT * FROM Customers ORDER BY Country;
```

ORDER BY DESC
```SQL
SELECT * FROM Customers ORDER BY Country DESC;
```

ORDER BY Several Columns Example
```SQL
SELECT * FROM Customers ORDER BY Country DESC, CustomerName ASC;
```

# 6. INSERT INTO
The INSERT INTO statement is used to insert new records in a table.
```SQL
INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
INSERT INTO table_name VALUES (value1, value2, value3, ...);
```

Examples:
```SQL
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
INSERT INTO Customers (CustomerName, City, Country) VALUES ('Cardinal', 'Stavanger', 'Norway');
```

# 7. NULL Values
A field with a NULL value is a field with no value.

If a field in a table is optional, it is possible to insert a new record or update a record without adding a value to this field. Then, the field will be saved with a NULL value.

```SQL
SELECT column_names FROM table_name WHERE column_name IS NULL;
SELECT column_names FROM table_name WHERE column_name IS NOT NULL;
```

# 8. UPDATE
The UPDATE statement is used to modify the existing records in a table. 

Be careful when updating records in a table! Notice the WHERE clause in the UPDATE statement. The WHERE clause specifies which record(s) that should be updated. If you omit the WHERE clause, all records in the table will be updated!

```SQL
UPDATE Customers SET ContactName = 'Alfred Schmidt', City= 'Frankfurt' WHERE CustomerID = 1;
UPDATE Customers SET ContactName='Juan' WHERE Country='Mexico';
```

# 9. DELETE
The DELETE statement is used to delete existing records in a table.
```SQL
DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
DELETE * FROM table_name;
```

# 10. LIMIT
The LIMIT clause is used to specify the number of records to return.
```SQL
SELECT column_name(s) FROM table_name WHERE condition LIMIT number;
```

Example:
```SQL
SELECT * FROM Customers WHERE Country='Germany' LIMIT 3;
```

# 11. MIN/MAX
## 11.1 MIN
The MIN() function returns the smallest value of the selected column.
```SQL
SELECT MIN(column_name) FROM table_name WHERE condition;
```
Example
```SQL
SELECT MIN(Price) AS LargestPrice FROM Products;
```

## 11.2 MAX
The MAX() function returns the largest value of the selected column.
```SQL
SELECT MAX(column_name) FROM table_name WHERE condition;
```
Example
```SQL
SELECT MAX(Price) AS LargestPrice FROM Products;
```

# 12. COUNT/AVG/SUM
## 12.1 COUNT
The COUNT() function returns the number of rows that matches a specified criteria.
```SQL
SELECT COUNT(column_name) FROM table_name WHERE condition;
```

## 12.2 AVG
The AVG() function returns the average value of a numeric column.
```SQL
SELECT AVG(column_name) FROM table_name WHERE condition;
```

## 12.3 SUM
The SUM() function returns the total sum of a numeric column.
```SQL
SELECT SUM(column_name) FROM table_name WHERE condition;
```

# 13. Like
The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

There are two wildcards used in conjunction with the LIKE operator:
* % - The percent sign represents zero, one, or multiple characters
* _ - The underscore represents a single character

```SQL
SELECT column1, column2, ... FROM table_name WHERE columnN LIKE pattern;
```

Examples:

| LIKE Operator	| Description |
| ----- | ------ |
|WHERE CustomerName LIKE 'a%'|	Finds any values that start with "a"|
|WHERE CustomerName LIKE '%a'|	Finds any values that end with "a"|
|WHERE CustomerName LIKE '%or%'|	Finds any values that have "or" in any position|
|WHERE CustomerName LIKE '_r%'|	Finds any values that have "r" in the second position|
|WHERE CustomerName LIKE 'a_%_%'|	Finds any values that start with "a" and are at least 3 characters in length|
|WHERE ContactName LIKE 'a%o'|	Finds any values that start with "a" and ends with "o"|

```SQL
SELECT * FROM Customers WHERE CustomerName LIKE 'a%';
```

# 14. IN
The IN operator allows you to specify multiple values in a WHERE clause. The IN operator is a shorthand for multiple OR conditions.
```SQL
SELECT column_name(s) FROM table_name WHERE column_name IN (value1, value2, ...);
SELECT column_name(s) FROM table_name WHERE column_name IN (SELECT STATEMENT);
```

Examples:
```SQL
SELECT * FROM Customers WHERE Country IN (SELECT Country FROM Suppliers);
SELECT * FROM Customers WHERE Country NOT IN ('Germany', 'France', 'UK');
```

# 15. BETWEEN
The BETWEEN operator selects values within a given range. The values can be numbers, text, or dates.

The BETWEEN operator is inclusive: begin and end values are included. 
```SQL
SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value1 AND value2;
```

Examples:
```SQL
SELECT * FROM Products WHERE Price NOT BETWEEN 10 AND 20;
SELECT * FROM Products WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni' ORDER BY ProductName;
```

# 16. Aliases
SQL aliases are used to give a table, or a column in a table, a temporary name.

Aliases are often used to make column names more readable.

An alias only exists for the duration of the query.

```SQL
SELECT column_name AS alias_name FROM table_name;
SELECT column_name(s) FROM table_name AS alias_name;
```

Example:
```SQL
SELECT o.OrderID, o.OrderDate, c.CustomerName FROM Customers AS c, Orders AS o WHERE c.CustomerName="Around the Horn" AND c.CustomerID=o.CustomerID;
```

# 17. Inner Join
Inner join is also known as join. The (INNER) JOIN keyword selects records that have matching values in both tables.
```SQL
SELECT column_name(s) FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;
```
Example:
```SQL
SELECT Orders.OrderID, Customers.CustomerName FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```
Inner join three tables:
```SQL
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName FROM ((Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID) INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);
```

# 18. LEFT JOIN
The LEFT JOIN keyword returns all records from the left table (table1), and the matched records from the right table (table2). The result is NULL from the right side, if there is no match.
```SQL
SELECT column_name(s) FROM table1 LEFT JOIN table2 ON table1.column_name = table2.column_name;
```
Example:
```SQL
SELECT Customers.CustomerName, Orders.OrderID FROM Customers LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID ORDER BY Customers.CustomerName;
```

# 19. RIGHT JOIN
The RIGHT JOIN keyword returns all records from the right table (table2), and the matched records from the left table (table1). The result is NULL from the left side, when there is no match.
```SQL
SELECT column_name(s) FROM table1 RIGHT JOIN table2 ON table1.column_name = table2.column_name;
```
Example
```SQL
SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID ORDER BY Orders.OrderID;
```

# 20. SELF JOIN
A self JOIN is a regular join, but the table is joined with itself.

```SQL
SELECT column_name(s) FROM table1 T1, table1 T2 WHERE condition;
```
Example:
```SQL
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City FROM Customers A, Customers B WHERE A.CustomerID <> B.CustomerID AND A.City = B.City ORDER BY A.City;
```

# 21. GROUP BY
The GROUP BY statement is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.

Select column can shoud be the columns in **aggregated functions or group by**.
```SQL
SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) ORDER BY column_name(s);
```
Example:
```SQL
SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID GROUP BY ShipperName;
```

# 22. Having
The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.
```SQL
SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) HAVING condition ORDER BY column_name(s);
```

Example:
```SQL
SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING COUNT(CustomerID) > 5;
```
