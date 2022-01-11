# order by 를 이용해 정렬하여 데이터를 출력하는 방법

column 명을 이용하여 정렬

```sql
select * from exam_result 
order by math;
```

`math`를 기준으로 오름차순으로 정렬

내림차순으로 정렬하고 싶으면 

```sql
select * from exam_result
order by math desc;
```

이렇게 뒤에 `desc` 를 붙이면 된다.

`math` 대신 평균을 구하고 싶으면 이렇게도 가능하다.

```sql
select * from exam_result
order by (math+english+korean)/3 desc;
-- 3개의 열의 평균
```

> order by 뒤에 숫자가 붙어 있는 경우가 있다.  
> order by 3 은
> 3번 column을 이용하여 정렬이라는 뜻이다.

