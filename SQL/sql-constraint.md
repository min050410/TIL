# SQL 제약조건

어떤 규칙에 따라 올바른 데이터만 입력받고, 규칙에 어긋나거나 잘못된 데이터는 입력 및 변경이 되지 않도록 하는 조건을 말한다.

> 이러한 제약조건의 역할로 인해 DB내 테이블이 가진 데이터의 신뢰도와 정확도가 증가한다.

|제약조건 6가지|
|-|
primary key|
foreign key|
not null|
unique|
check|
default|

### 👉 Primary key
`primary key`란 칼럼의 중복을 막고, `null`을 허용하지 않으며, 각 로우를 특정할 수 있는 구분키로 사용된다.

not null + unique의 의미를 가지고 있다.

> 테이블당 primary key는 하나만 생성이 가능하다

```sql
alter table schema.name.table_name
            add primary key(col1, col2, ...);

-- drop
alter table schema_name.table_name drop primary key;
```

> primay key 를 설정할 때에는 각 데이터 row의 유일성이 보장되어야 한다. 중요

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbsx5Nr%2FbtqFujfcLQO%2F0JRGubnSXoXyLQMSKk3eG0%2Fimg.png)

이 사진의 경우 하나의 컬럼이 테이블의 각 row를 특정할 수 있다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F2io4E%2FbtqFvgI1Juw%2FdksUl8hbKc2Dg3aJY5g0j1%2Fimg.png)

하지만 이 사진의 경우 겹치는 값이 있어 두개의 컬럼이 테이블의 각 `row`를 특정한다.  
이렇게 `n`개의 컬럼이 `row`를 특정하기도 한다.

```sql
add primary key(col1, ...);
-- 여기 col이 추가가 된다면 여러개의 컬럼이 row를 특정할수 있게 된다
```

### 👉 Foreign key
`foreign key`는 어떤 테이블의 칼럼 값은 다른 테이블의 칼럼 값을 __참조__ 해야 한다는 제약 조건이다.

예전에 `flask` 프로젝트를 진행하면서 `foreign key`를 유저가 자신이 쓴 게시글을 찾을 때 쓴 적이 있었다.  
유저 칼럼이 있다면 게시글 칼럼에 참조해 데이터를 가져오기 위해서 `foreign key`를 사용한다. 또 존재하지 않는 유저는 게시글에 값이 들어갈 수 없어 안정성을 유지할 수 있다. 

```sql
alter table order
        add constraint order_customer_id_fk
            foreign key (customer_id) references customer (customer_id);

-- drop 
alter table order drop key order_customer_id_fk;
```

### 👉 Not null
`not null`은 말 그대로 `null` 값이 들어올 수 없다고 제약 조건을 명시하는 것이다.

```sql
alter table schema_name.table_name modify col1 int not null;

-- 해제
alter table schema_name.table_name modify col1 int null;
```

### 👉 Unique
`unique` 제약조건은 설정된 칼럼에는 중복된 값이 들어가지 못하게 설정하는 제약조건이다.
`primary key`와 혼동할 수 있으나, `primary key`를 제외하고 테이블 내 다른 칼럼 중에 중복된 값이 들어오면 안되는 경우에 설정할 수 있다.

```sql
alter table schema_name.table_name
            add constraint table_pk
                unique (col1, col2);

-- drop
alter table schema_name.table_name drop key table_pk;
```

### 👉 Check
어떤 칼럼 값이 `check` 제약 조건으로 지정된 값 이외 다른 값이 들어오지 못하도록 하는 제약조건이다.

성별 칼럼, Yes no 칼럼, 온도 칼럼, 나이 칼럼 등등  
특정 범위를 지정하고 싶은 칼럼에 설정한다.

```sql
alter table schema_name.table_name
        add constraint CHK_PersonAge check (col1 >= 18);

-- drop
alter table schema_name.table_name
drop constraint CHK_PersonAge;
```

### 👉 Default

얘는 제약조건이라고 부르기에는 애매하다. 규칙을 가진다기 보다 초깃값을 설정하는 것이라고 보면 편하다. 

```sql
alter table customer alter column name set default 'N';

-- drop
alter table customer alter column name drop default;
```



