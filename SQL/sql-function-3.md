# SQL function(3) - 숫자 함수

숫자 함수에는 대표적으로 `6가지`가 있다.

### 👉 round 함수

> 숫자를 반올림 한 후 출력

```sql
select round(112.3456,1),round(112.3456,2),round(112.3456,-1) from dual;

-- 출력값: 112.3, 112.35, 110
```

> from dual은 자체에서 제공되는 테이블이고 간단하게 함수를 이용해서 계산 결과값을 확인 할 때 사용하는 테이블이다.

### 👉 truncate 함수

> round 함수와 동일 ( 사용법도 같음 )

### 👉 mod 함수

> 나머지를 결과로 출력

```sql
select mod(26,3),mod(10,9),mod(4,2) from dual;

-- 출력값: 2, 1, 0
```

### 👉 ceil 함수

> ceil 함수는 입력된 숫자보다 **크면**서도, 가장 **가까운** 정수가 출력됨.

```sql
select ceil(12.6),ceil(11.5),ceil(16.3) from dual;

-- 출력값: 13, 12, 17 
```

### 👉 floor 함수

> floor 함수는 ceil 함수와 반대 개념이다.  
입력된 값보다 **작으면서** 가장 **가까운** 정수가 출력됨.

```sql
select floor(12.6),floor(11.5),floor(16.3) from dual;

-- 출력값 : 12, 11, 16
```

### 👉 power 함수

> power 함수는 첫 번째 입력된 값을 두번째 입력값 만큼 제곱 하여 출력을 함

```sql
select power(1,2),power(2,3),power(3,5) from dual;

-- 출력값 : 1, 8, 248
```

다른 숫자 함수는 [여기](https://dev.mysql.com/doc/refman/8.0/en/numeric-functions.html)에서 확인해보자










