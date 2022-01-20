# SQL function(4) - 복수행함수와 group by

|제목|
|-|
|예제|
|설명|

순으로 보시면 됩니다!  

### count()
```sql
select count(*) from salary
```

count() 함수는 전체 칼럼을 대상으로 총 건수를 계산해서 반환한다.

### sum()
```sql
select sum(salary) from salary;
```

sum() 함수는 입력된 데이터들의 합계 값을 구해서 반환하는 함수이다.

### avg()
```sql
select avg(salary) from salary;
```
avg() 함수는 입력된 데이터 값의 평균 값을 반환하는 함수이다.

### max(), min()
```sql
select max(salary), min(salary) from salary;
```
최댓값과 최솟값을 구하는 함수이다.

### stddev()
```sql
select stddev(salary) from salary;
```
표준편차를 구하는 함수이다. 함수 하나로 표준편차를 쉽게 구할 수 있다.

### variance()
```sql
select variance(salary) from salary;
```
분산을 구하는 함수이다.

## 📑 복수행 함수에서 group by 사용하기

group by 란? 일정 부분만 묶어서 그 부분만 복수행 함수를 실행한다.

예를 들면, 같은 데이터끼리 묶어 sum()을 이용해 더하게 하고 싶을 때 사용한다.  
기본적으로는 이렇게 컬럼명을 줘서 사용한다.

```sql
select do, avg(budget_value) as 예산평균, sum(budget_value) as 예산합계 from class.budget 
group by do;
```

`do` 라는 컬럼 안의 같은 데이터 끼리 묶어서 값이 나오게 된다.  
예를 들면, 서울 특별시가 포함된 줄이 3줄 있었다면 하나로 묶어서 한줄로 나오게 된다.

> group by 사용시 주의할 점  
`group by` 절에서는 단순히 컬럼 명만 사용할 수도 있지만 함수를 이용해서도 group by를 사용할 수 있는데 이 때에는 `select` 절에도 그 함수 그대로를 써줘야 한다.

```sql
select do, avg(budget_value) as 예산평균, sum(budget_value) as 예산 합계
from budget
group by if(do in('서울특별시', '경기도'), '수도권', '지방')
```

이렇게 하면 안된다! 

```sql
select if(do in ('서울특별시','경기도'), '수도권','지방') as 지역구분, avg(budget_value) as 예산평균, sum(budget_value) as 예산 합계
from budget
group by if(do in('서울특별시', '경기도'), '수도권', '지방')
```

이렇게 `select` 절에도 함수를 사용해야 원하는 값이 나온다.

> 번외 
#### if(do in('서울특별시', '경기도'), '수도권', '지방') 분석하기!

SQL에서는 if문을 if(조건, 참, 거짓)으로 쓴다.

따라서 위의 문법은 먼저 `do` 테이블 안에 '서울특별시'나 '경기도'가 있는지 검사하고  
있다면 수도권으로  
없다면 지방으로 그룹핑하라는 문법이다



