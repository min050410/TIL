# W3C SQL 연습문제 풀어보기

[여기](https://www.w3schools.com/sql/exercise.asp?filename=exercise_select1)에서 풀어볼 수 있어요

|1. |Customers 테이블에서 모든 열을 가져옵니다.|
|-|-|
```sql
SELECT * FROM Customers
```

|2. |테이블에서 열(City)를 선택하는 명령문을 작성하십시오 .|
|-|-|
```sql
SELECT City FROM Customers
```

|3. |테이블의 열에서 Country와 다른 열을 모두 선택 합니다.|
|-|-|

```sql  
SELECT DISTINCT Country FROM Customers;
```

|4. |City열에 "Berlin" 값이 있는 모든 레코드를 선택하십시오.|
|-|-|
```sql
SELECT * FROM Customers
WHERE City = "Berlin";
```

|5. |키워드를 사용하여 "Berlin"이 아닌 모든 레코드를 선택하십시오.|
|-|-|
```sql
SELECT * FROM Customers
WHERE NOT City = 'Berlin';
```

|6. |CustomerID 열의 값이 32 인 모든 레코드를 선택합니다.|
|-|-|
```sql
SELECT * FROM Customers
where CustomerID = 32;
```

|7. |City 열 값이 'Berlin' 이고 PostalCode 열 값이 12209인 모든 레코드를 선택하십시오.|
|-|-|
```sql
SELECT * FROM Customers
WHERE City = 'Berlin'
AND PostalCode = 12209;
```

|8. |City열에 'Berlin' 또는 'London' 값이 있는 모든 레코드를 선택하십시오 .|
|-|-|
```sql
SELECT * FROM Customers
WHERE City = 'Berlin'
OR City = 'London';
```

|9. |테이블 에서 모든 레코드를 선택하고 결과를 City 열을 기준으로 알파벳순으로 정렬합니다.|
|-|-|
```sql
SELECT * FROM Customers
ORDER BY City;
```

|. ||
|-|-|
```sql

```

|. ||
|-|-|
```sql

```

|. ||
|-|-|
```sql

```

|. ||
|-|-|
```sql

```

|. ||
|-|-|
```sql

```

|. ||
|-|-|
```sql

```

|. ||
|-|-|
```sql

```


