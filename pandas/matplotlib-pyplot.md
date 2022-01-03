# pyplot로 그래프 그리기

+ plt.plot() 
  + 선모양 정하기 
    + **색상**
      - b(파란색), g(초록색), r(빨간색), c(청록색), y(노란색), k(검은색), w(흰색)
    + **마커**
      - o(원), v(역삼각형), ^(삼각형), s(네모), +(플러스), .(점)
    + **선스타일**
      - \-(solid line), --(dashed line ), -. (dash-dot line), : (dotted line )

+ **그래프 크기 조절**
  + plt.figure(figsize=(가로,세로)) 
    - figsize를 이용하여 가로, 세로 길이 조절 가능 (inch 단위)

+ **그래프 제목 추가하기**
  + plt.title('그래프제목') 
  + plt.xlabel('x축 제목')
  + plt.ylabel('y축 제목')

+ **그리드 (grid)**
  + grid() 함수의 첫번째 파라미터를 True로 설정하면 그래프에 그리드 (grid)가 표시 
  + alpha:  그리드의 투명도를 설정
    - 0으로 설정하면 투명하게, 1은 불투명하게 표시
  + linestyle : 선의 스타일을 대쉬 (Dashed)로 설정 

+ **수평 / 수직선 그리기**
  + plt.axvline(x, color) : 축을 가로지르는 세로 선 생성
  + plt.axhline(y, color) : 축을 가로지르는 가로 선 생성

+ **글자 쓰기**
  + plt.text(x, y, s, fontsize) : 원하는 위치에 텍스트 생성

+ **x축 눈금 표시 및 회전**
  + plt.xticks(범위, labels=레이블리스트, rotation=90)

+ **범례 표시**
  + plt.legend(loc='best')

```python
plt.figure(figsize=(10,7)) #그래프의 크기 조절하기 => 튜플의 형태 10인치, 7인치
plt.plot(df['출생아수'], 'go--', label='출생아수')
plt.plot(df['사망자수'], 'bx-', label='사망자수')
plt.plot(df['자연증가수'], 'r-', label='자연증가수')
plt.grid(True) #줄 표시
plt.xticks(df.index, labels=df['년도'], rotation=90) #x축 눈금 표시
plt.axvline(x = df[df['년도']==2000].index, color='r') # 선 추가
plt.legend() #범례 추가
plt.show()
```

### 여러가지 그래프 
+ 막대 그래프 : plt.bar(x, y)
+ 산점도 그래프 : plt.scatter(x, y)
+ 히스토그램 : plt.hist(value)
+ 박스플롯 : plt.boxplot(value)

> 막대 그래프와 산점도 그래프는 x값이 있어야 한다

### 판다스 내장 그래프
```python
df.plot()
```

판다스 내장 그래프는 기존과 다 동일하지만 크기 설정할 때만
```python
df[['레이블1', '레이블2','레이블3']].plot(figsize=(10,7)) # 이렇게 해야 한다.
```