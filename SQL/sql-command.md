# SQL 명령어 종류

- DDL - Data Definition Language (데이터 정의 언어)
- DML - Data Manipulation Language (데이터 조작 언어)
- DCL - Data Control Language (데이터 제어 언어)

### DDL
|제목|설명|
|-|-|
|CREATE|데이터베이스 내 개체 (테이블, 인덱스 제약조건 등)을 생성할 때|
|DROP|데이터베이스 내 개체를 삭제할 때|
|ALTER|데이터베이스 내 개체의 속성 및 정의를 변경할 때|
|RENAME|데이터베이스 내 개체의 이름을 변경 할 때|
|TRUNCATE|테이블 내 모든 데이터를 빠르게 삭제할 때|

### DML
|제목|설명|
|-|-|
|INSERT|특정 테이블에 데이터를 신규로 삽입할 때|
|UPDATE|특정 테이블 내 데이터의 전체, 또는 일부를 새로운 값으로 갱신할 때|
|DELETE|특정 테이블 내 데이터의 전체, 또는 일부를 삭제할 때|
|SELECT|특정 테이블 내 데이터의 전체 또는 일부를 획득할 때|

### DCL
|제목|설명|
|-|-|
|GRANT|데이터베이스 사용자에게 특정 작업의 수행 권한을 부여할 때|
|REVOKE|GRANT의 반대|
|SET TRANSACTION|트랜잭션 모드로 설정 할 때|
|BEGIN|트랜잭션의 시작을 의미|
|COMMIT|트랜잭션을 실행 할 때|
|ROLLBACK|트랜잭션을 취소 할 때|
|SAVEPOINT|롤백 지점을 설정 할 때|
|LOCK|테이블 자원을 점유 할 때|