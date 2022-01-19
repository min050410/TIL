# SQL subquery

### ⌨️ subquery 종류

|사용 위치|명칭|
|-|-|
`select` 절|스칼라 서브쿼리(Scalar Subquery)
`from` 절|인라인 뷰 (inline view)
`where` 절|중첩 서브쿼리 or 서브쿼리

### 1. Scalar Subquery

```sql
select name                        as 학생이름, 
    (select major_title 
    from class.major b 
    where b.major_id = a.major_id) as 학과명 
from class.student a;
```

스칼라 서브 쿼리의 where절에는 메인 쿼리의 칼럼 값이 들어간다. 그리고 그 값으로 스칼라 서브 쿼리에서 검색된 값이 출력 값으로 나오게 된다. 

> 주의점 : 쿼리 결과가 무조건 하나의 행으로만 나와야 함

### 2. Inline view

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FnyHvQ%2FbtqD5Jr9t8i%2FhmTueWjXrAZSwRlSBKKzB0%2Fimg.png)

인라인 뷰는 하나의 테이블이라고 생각하고 쓰면 편하다, inline view를 이용하여 join도 하고 where절에 조건도 걸수 있다.

```sql
select a.name        as 학생이름
       b.major_title as 학과명
from class.student a, (select major_title, major_id from class.major) b
-- 이렇게 하나의 테이블로 사용할 수 있다!
where a.major_id = b.major_id
```

### 3. subquery (where절에 사용)

단일행 서브 쿼리
```sql
select name as 학생이름
from class.student
where major_id = (select major.major_id from class.major where major_title = '컴퓨터공학과');
```

복수행 서브 쿼리
```sql
select name as 학생이름
from class.student
where major_id in (select major.major_id from class.major where major_title in ('컴퓨터공학과', '국문학과'))
```

> scala 서브쿼리 vs join  
> join을 사용하는 것이 대부분 sql에서 더욱 좋은 성능을 나타낸다.



