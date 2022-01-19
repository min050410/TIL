# SQL 테이블 병합하는 방법

`insert into on duplicate key` 문은 `oracle`에서 `merge`문과 같은 기능을 가지고 있다.
어떤 데이터를 입력을 하는데, 대상 테이블에 해당 키에 해당하는 데이터가 없으면 `insert`문을 실행해 입력을 하고, 해당 키가 이미 대상 테이블에 있는 경우에는 다른 칼럼들을 `update`하여 값을 경신하겠다는 의미이다.

### 📑 insert into on duplicate key 문 사용 예제
```sql
insert into insert_test
select *
from insert_test2 b
on duplicate key update cont    = b.cont,
                        name    = b.name,
                        tel_num = b.telnum,
                        input_date = now();
```

`on duplicate` 즉, 중복된다면 `update`하라는 의미이다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLPBPs%2FbtqEAC0vSMW%2FZh2YEmjenIF5as5KD8bG6k%2Fimg.png)

### 📑 insert into on duplicate key 문 사용 예제 2
```sql
insert into insert_test
values (8, '사회적 거리두기를 실천 합시다.', '손흥민', 1012345678, now())
on duplicate key update cont = '사회적 거리두기를 실천 합시다.',
                        name = '손흥민',
                        tel_num = 1012345678,
                        input_date = now();
```

이렇게 `on duplicate key update`를 이용한다면 `table`을 쉽게 병합할 수 있다.

                    