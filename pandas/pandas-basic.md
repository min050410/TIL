# pandas

파이썬에서 사용하는 데이터 분석 라이브러리
- 행과 열로 이루어진 데이터 객체를 만들어 다룰 수 있게 되며 보다 안정적으로 대용량의 데이터들을 처리하는데 매우 편리한 도구
- `NumPy`를 기반으로 구축되었으며 과학 컴퓨팅 환경 내에서 다른 많은 타사 라이브러리와 잘 통합되도록 설계
- 많은 기능을 가진 데이터 구조
    - 다양한 방식으로 색인된 데이터를 다룰 수 있는 기능
    - 시계열 데이터와 비시계열 데이터를 함께 다룰 수 있는 통합 자료 구조
    - 누락된 데이터를 유연하게 처리할 수 있는 기능
    - SQL 같은 일반 데이터베이스처럼 데이터를 합치고 관계연산을 수행하는 기능

### pandas 자료 구조
- Series
    - 1차원 자료구조
    - index로 value를 구분함
- DataFrame
    - 2차원 자료구조
    - DataFrame은 행과 열이 있는 테이블 데이터

### pandas 시작하기
```python
import pandas as pd
df = pd.read_csv(‘파일명‘, engine='python', encoding='cp949' )
```

### DataFrame 살펴보기
- `DataFrame`의 정보 : df.info()
    - 데이터프레임의 전반적인 정보
- `DataFrame`의 크기 확인 : df.shape 속성
    -(행 열) 크기를 확인하기
- `DataFrame`의 원소의 총 개수 : df.size 속성
- `DataFrame`의 개수 확인 : df.count()

### DataFrame 기본 조회
```python
# 상위 3개 조회 하위는 tail()
df.head(3)

년도	출생아수(명)	사망자수(명)	혼인건수(건)
0	1970	1006645	258589	295137
1	1971	1024773	237528	239457
2	1972	952780	210071	244780
```
### DataFrame의 인덱스
- 열의 인덱스 : df.columns
- 행의 인덱스 : df.index
- df의 인덱스 변경 
    - 열 인덱스 변경 : df.column = [열명 인덱스]
    - 열항목 중 하나를 인덱스로 사용 : df.set_index(열명)
    - 인덱스를 일반 데이터 열로 전환 : df.reset_index()

```python
lt = [item if item=="년도" else item[:-3] for item in lt]
# 열 인덱스 변경(type: list)
df.columns = lt
```

### DataFrame 기초 통계 메소드
- mean() : 평균
- max() : 최대
- min() : 최소
- std() : 표준편차

- 요약 : df.describe()

### DataFrame 추출하기
- 열 자료 가져오기 : df[]

- 인덱스명으로 특정 항목 가져오기 : df.loc[행인덱스, 열인덱스]

- 인덱스 위치값으로 특정 항목 가져오기 : df.iloc[행인덱스순서, 열인뎃스순서]


> .loc와 .iloc의 차이??
```python
# 내용으로 가져옴 
df.loc[1971:1972, '출생아수':'사망자수']
# 위치 값으로 가져옴
df.iloc[1:3, 0:2]
```
> 동시에 가져오는 법 
```python
df2 = df.loc[[2015, 2020], ['출생아수', '혼인건수']]

	출생아수	혼인건수
년도		
2015	438420	302828
2020	272337	213502
```

### DataFrame 정렬
- 행 인덱스로 정렬 : df.sort_index(axis=n), n생략 또는 0:행, 1:열
- 열 값으로 정렬 : df.sort_values()
- 내림차순 옵션 : ascending=False

```python
#index별 내림차순
df.sort_index(ascending=False)
```

### 데이터프레임 새로운 열 생성
- df['새로운열명'] = 시리즈데이터

### 외부 파일로 저장
- csv 쓰기
```
df.to_csv(‘파일명‘, index=False)
```

- 엑셀 쓰기 
```
df.to_excel(‘파일명‘)
```


