# SQL join 정의 및 종류 알아보기

`join`을 사용해서 여러 테이블이나 스키마에 분산되어 있는 데이터를 다음과 같이 하나의 `view`로 출력할 수 있다. 

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlUcxR%2FbtqDsbREq6y%2FBkpMGIKF3dkwkdFBGPTRrK%2Fimg.png)

### join의 종류 알아보기
### 👉 카티션곱 join
카티션곱 `join`이란 `join`할 때 `join` 조건을 기술하지 않고 하는 `join`을 말한다. 카티션곱 `join`의 결과는 두 테이블의 row`건수를 서로 곱한 것만큼의 결과를 출력한다. 

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLT561%2FbtqDrk9fLLB%2FnXssCWMn9uc0UloMSbNCXk%2Fimg.png)

### 👉 equi join
`equal` 연산자를 사용하여 양쪽에 다 존재하는 값만 결과로 출력하는 `join` 방법이다.
__inner join__ 이라고도 불린다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcOUJEt%2FbtqDvhcldZD%2FkrcIKZzZWLui0kYK5yhKzK%2Fimg.png)

### 👉 outer join

`Outer join`은 `left outer join`, `right outer join`, `full outer join`으로 구분된다.
`left outer join`과 `right outer join` 의 경우 어느 한쪽의 데이터를 모두 출력 한 뒤에 조건이 맞는 데이터만 다른 쪽에 출력을 하는 것을 말한다. 조건에 맞지 않는 데이터 옆에는 null이 출력된다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FRTMuT%2FbtqDVwtxZRx%2F4gVRW9V3kxmiJQLCPf7UV1%2Fimg.png)

### 👉 self join

`self join`은 한 테이블이 자기 자신과 `join`을 다시 하는 경우를 말한다. 

### join 사용법

### 📑 Cartesian product 

```sql 
-- mysql syntax
select major_id,
       major_title,
       prfs_id,
       name
from class.major m, class.processor p;
```

```sql
-- ansi sql syntax
select major_id,
       major_title,
       prfs_id,
       name
from class.major m cross join class.professor p;
```

### 📑 inner join
```sql
select name as 교수이름, major_title as 학과명
from class.professor p, class.major m
where p.bl_major_id = m.major_id;
```

`table`이 3개일때는 이렇게 `and`를 이용한다.
```sql
select name as 학생이름, name as 교수이름, major_title as 학과명
from class.student s, class.major m, class.professor p
where s.bl_prfs_id = p.prfs_id
  and p.bl_major_id = m.major_id
```

### 📑 outer join

```sql
select s.name, s.bl_prfs_id, p.name, p.prfs_id
from class.student s
        left outer join class.professor p 
            on s.bl_prfs_id = p.prfs_id
```
    


