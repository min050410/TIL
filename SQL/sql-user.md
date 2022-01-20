# SQL 계정별 권한 확인, 적용, 부여, 회수 계정 생성

### 계정 목록 보기
```sql
select host, user from user;
```
### 계정 생성 방법
```sql
create user 'user'@'127.0.0.1' identified by 'Password';
-- localhost 에서만 접속 허용

create user 'user'@'%' identified by 'Password';
-- everywhere 접속 허용
```
### 유저별 권한 부여
```sql
grant all privileges on TableName.* to 'user'@'127.0.0.1';
-- localhost에서만 허용

grant select on testDB.* to 'user'@'%';
-- everywhere 허용
```
### 유저별 권한 확인
```sql
show grants for 'user'@'접속위치';
```
### 유저별 권한 회수
```sql
revoke all on db_name.table_name FROM 'user'@'접속위치';
```
### 계정삭제
```sql
drop user 'user'@'접속위치';
```
