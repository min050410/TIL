# SQL view 알아보기

### ⌨️ view

`view`는 가상의 테이블을 의미한다.  
`select subquery` 때 `inline view`가 있었는데

그때 괄호 안에 있는 `select`문은 `inline view` 라고 이야기 한다.

![](https://t1.daumcdn.net/cfile/tistory/99F52D3E5F1E578216)

### ⌨️ 왜 view를 쓸까?

그냥 테이블을 쓰면 되지 왜 `inline view`를 쓰는 걸까? 이유는 보안과 함께 사용자의 편의성을 높아기 위함이다.

또한 여러 테이블을 조인할 시에 `view` 테이블을 통하면 SQL을 어느정도 간소화 시킬 수 있다. 또한 복잡한 SQL을 편리하게 재생성 할 수 있는 장점이 있다. 

>  View는 alter 명령어를 사용할 수 없으며, view의 내용을 수정하고 싶으면 drop & create를 반복해야 한다.

### ⌨️ view 생성 및 삭제 예제

```sql
create view 뷰이름 as select 구문;

-- delete
drop view 뷰이름;
```

