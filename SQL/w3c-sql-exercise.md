# W3C SQL 연습문제 풀어보기

[여기](https://www.w3schools.com/sql/exercise.asp?filename=exercise_select1)에서 풀어볼 수 있어요

### Content
- Select 
- Where
- Order by
- Insert
- Null
- Update
- Delete
- Functions
- Like
- Wildcards
- In 
- Between
- Alias 
- Join
- Group by
- Databases

총 51문제 

> 틀린 문제(복습) : DISTINCT,  Wildcards,  Join, Alter

### Select

|1. |Insert the missing statement to get all the columns from the Customers table.|
|-|-|
```sql
SELECT * FROM Customers
```


|2. |Write a statement that will select the City column from the Customers table.|
|-|-|
```sql
SELECT City FROM Customers
```

|3. |Select all the different values from the Country column in the Customers table.|
|-|-|

```sql  
SELECT DISTINCT Country FROM Customers;
```

### Where

|4. |Select all records where the City column has the value "Berlin".|
|-|-|
```sql
SELECT * FROM Customers
WHERE City = "Berlin";
```

|5. |Use the NOT keyword to select all records where City is NOT "Berlin".|
|-|-|
```sql
SELECT * FROM Customers
WHERE NOT City = 'Berlin';
```

|6. |Select all records where the CustomerID column has the value 32.|
|-|-|
```sql
SELECT * FROM Customers
where CustomerID = 32;
```

|7. |Select all records where the City column has the value 'Berlin' and the PostalCode column has the value 12209.|
|-|-|
```sql
SELECT * FROM Customers
WHERE City = 'Berlin'
AND PostalCode = 12209;
```

|8. |Select all records where the City column has the value 'Berlin' or 'London'.|
|-|-|
```sql
SELECT * FROM Customers
WHERE City = 'Berlin'
OR City = 'London';
```

### Order by

|9. |Select all records from the Customers table, sort the result alphabetically by the column City.|
|-|-|
```sql
SELECT * FROM Customers
ORDER BY City;
```

|10. |Select all records from the Customers table, sort the result reversed alphabetically by the column City.|
|-|-|
```sql
SELECT * FROM Customers
ORDER BY City DESC;
```

|11. |Select all records from the Customers table, sort the result alphabetically, first by the column Country, then, by the column City.|
|-|-|
```sql
SELECT * FROM Customers
ORDER BY Country, City;
```

### Insert

|11. |Insert a new record in the Customers table.|
|-|-|
```sql
INSERT INTO Customers ( CustomerName, Address, City, PostalCode,Country) 
VALUES(
    'Hekkan Burger',
    'Gateveien 15',
    'Sandnes',
    '4306',
    'Norway'
);
```

### Null

|12. |Select all records from the Customers where the PostalCode column is empty.|
|-|-|
```sql
SELECT * FROM Customers
WHERE PostalCode IS NULL;
```

|13. |Select all records from the Customers where the PostalCode column is NOT empty.|
|-|-|
```sql
SELECT * FROM Customers
WHERE PostalCode IS NOT NULL;
```

### Update

|14. |Update the City column of all records in the Customers table.|
|-|-|
```sql
UPDATE Customers
SET City = 'Oslo';
```

|15. |Set the value of the City columns to 'Oslo', but only the ones where the Country column has the value "Norway".|
|-|-|
```sql
UPDATE Customers
SET City = 'Oslo'
WHERE Country = 'Norway';
```

|16. |Update the City value and the Country value.|
|-|-|
```sql
UPDATE Customers
SET City = 'Oslo',
Country = 'Norway'
WHERE CustomerID = 32;
```

### Delete

|17. |Delete all the records from the Customers table where the Country value is 'Norway'.|
|-|-|
```sql
DELETE FROM Customers
WHERE Country = 'Norway';
```

|18. |Delete all the records from the Customers table.|
|-|-|
```sql
DELETE FROM Customers;
```

### Functions

|19. |Use the MIN function to select the record with the smallest value of the Price column.|
|-|-|
```sql
SELECT MIN(Price) 
FROM Products;
```

|20. |Use an SQL function to select the record with the highest value of the Price column.|
|-|-|
```sql
SELECT MAX(Price) 
FROM Products;
```

|21. |Use the correct function to return the number of records that have the Price value set to 18.|
|-|-|
```sql
SELECT COUNT(*)
FROM Products
WHERE Price = 18;
```

|22. |Use an SQL function to calculate the average price of all products.|
|-|-|
```sql
SELECT AVG(Price)                      
FROM Products;
```

|23. |Use an SQL function to calculate the sum of all the Price column values in the Products table.|
|-|-|
```sql
SELECT SUM(Price)
FROM Products;
```

### Like

|24. |Select all records where the value of the City column starts with the letter "a".|
|-|-|
```sql
SELECT * FROM Customers
WHERE City LIKE 'a%';
```

|25. |Select all records where the value of the City column ends with the letter "a".|
|-|-|
```sql
SELECT * FROM Customers
WHERE City LIKE '%a';
```

|26. |Select all records where the value of the City column contains the letter "a".|
|-|-|
```sql
SELECT * FROM Customers
WHERE City LIKE '%a%';
```

|27. |Select all records where the value of the City column starts with letter "a" and ends with the letter "b".|
|-|-|
```sql
SELECT * FROM Customers
WHERE City LIKE 'a%b';
```

|28. |Select all records where the value of the City column does NOT start with the letter "a".|
|-|-|
```sql
SELECT * FROM Customers
WHERE City NOT LIKE 'a%';
```

### Wildcards

|29. |Select all records where the second letter of the City is an "a".|
|-|-|
```sql
SELECT * FROM Customers
WHERE City LIKE '_a%';
```

|30. |Select all records where the first letter of the City is an "a" or a "c" or an "s".|
|-|-|
```sql
SELECT * FROM Customers
WHERE City LIKE '[acs]%';
```

|31. |Select all records where the first letter of the City starts with anything from an "a" to an "f".|
|-|-|
```sql
SELECT * FROM Customers
WHERE City LIKE '[a-f]%';
```

|32. |Select all records where the first letter of the City is NOT an "a" or a "c" or an "f".|
|-|-|
```sql
SELECT * FROM Customers
WHERE City LIKE '[!acf]%';
```

### In

|33. |Use the IN operator to select all the records where Country is either "Norway" or "France".|
|-|-|
```sql
SELECT * FROM Customers
WHERE Country IN ('Norway','France');
```

|34. |Use the IN operator to select all the records where Country is NOT "Norway" and NOT "France".|
|-|-|
```sql
SELECT * FROM Customers
WHERE Country NOT IN ('Norway', 'France');
```

### Between

|35. |Use the BETWEEN operator to select all the records where the value of the Price column is between 10 and 20.|
|-|-|
```sql
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;
```

|36. |Use the BETWEEN operator to select all the records where the value of the Price column is NOT between 10 and 20.|
|-|-|
```sql
SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;
```

|37. |Use the BETWEEN operator to select all the records where the value of the ProductName column is alphabetically between 'Geitost' and 'Pavlova'.|
|-|-|
```sql
SELECT * FROM Products
WHERE ProductName 
BETWEEN 'Geitost' AND 'Pavlova';
```

### Alias

|38. |When displaying the Customers table, make an ALIAS of the PostalCode column, the column should be called Pno instead.|
|-|-|
```sql
SELECT CustomerName,
Address,
PostalCode AS Pno
FROM Customers;
```

|39. |When displaying the Customers table, refer to the table as Consumers instead of Customers.|
|-|-|
```sql
SELECT *
FROM Customers AS Consumers;
```

### Join

|40. |Insert the missing parts in the JOIN clause to join the two tables Orders and Customers, using the CustomerID field in both tables as the relationship between the two tables.|
|-|-|
```sql
SELECT *
FROM Orders
LEFT JOIN Customers
ON Orders.CustomerID = Customers.CustomerID;
```

|41. |Choose the correct JOIN clause to select all records from the two tables where there is a match in both tables.|
|-|-|
```sql
SELECT *
FROM Orders
INNER JOIN Customers
ON Orders.CustomerID=Customers.CustomerID;
```

|42. |Choose the correct JOIN clause to select all the records from the Customers table plus all the matches in the Orders table.|
|-|-|
```sql
SELECT *
FROM Orders
RIGHT JOIN Customers
ON Orders.CustomerID=Customers.CustomerID;
```

### Group by

|43. |List the number of customers in each country.|
|-|-|
```sql
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;
```

|44. |List the number of customers in each country, ordered by the country with the most customers first.|
|-|-|
```sql
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;
```

### Database

|45. |Write the correct SQL statement to create a new database called testDB.|
|-|-|
```sql
CREATE DATABASE testDB;
```

|46. |Write the correct SQL statement to delete a database named testDB.|
|-|-|
```sql
DROP DATABASE testDB;
```

|47. |Write the correct SQL statement to create a new table called Persons.|
|-|-|
```sql
CREATE TABLE Persons
 (
  PersonID int,
  LastName varchar(255),
  FirstName varchar(255),
  Address varchar(255),
  City varchar(255) 
);
```

|48. |Write the correct SQL statement to delete a table called Persons.|
|-|-|
```sql
DROP TABLE Persons;
```

|49. |Use the TRUNCATE statement to delete all data inside a table.|
|-|-|
```sql
TRUNCATE TABLE Persons;
```

|50. |Add a column of type DATE called Birthday.|
|-|-|
```sql
ALTER TABLE Persons
ADD Birthday DATE;
```

|51. |Delete the column Birthday from the Persons table.|
|-|-|
```sql
ALTER TABLE Persons
DROP COLUMN Birthday;
```
