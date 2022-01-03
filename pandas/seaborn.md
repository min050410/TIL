# Seaborn을 이용하여 그래프 그리기
+ `Matplotlib`을 기반으로 다양한 색상 테마와 통계용 차트 등의 기능을 추가한 시각화 패키지
+ 기본적인 시각화 기능은 `Matplotlib` 패키지에 의존하며 통계 기능은 `Statsmodels` 패키지에 의존
+ 데이터프레임으로 다양한 통계 지표를 낼 수 있는 시각화 차트를 제공하기 때문에 데이터 분석에 활발히 사용되고 있는 패키지
+ 다차원 데이터 분석시 고려 사항
  + 분석하고자 하는 데이터가 모두 실수 값인 경우
  + 분석하고자 하는 데이터가 모두 카테고리 값인 경우
  + 분석하고자 하는 데이터가 모두 실수 값과 카테고리 값이 섞여 있는 경우

```python
import seaborn as sns
```

### 시각화를 이용한 데이터 분포 확인
+ 범주형 : countplot
+ 수치형
  + 이산형 : barplot
  + 연속형 : kdeplot, histogram
+ 범주형 + 수치형 : boxplot, violinplot, etc
+ 수치형 + 수치형 : scatter
+ 범주형 + 범주형 : heatmap

### count plot
+ 각 **범주형 값**별로 데이터가 얼마나 있는지 표시
```python
sns.countplot(x='증감', data=df)
plt.show()
```

### barplot
+ **카테고리 값에 따른 실수 값**의 평균과 편차를 표시하는 기본적인 바 차트를 생성
+ 평균은 막대의 높이로, 편차는 에러바(error bar)로 표시

```python
sns.barplot(y='출생아수', data=df)
plt.show()
```

### scatter plot
+ 두 개의 수치값에 대한 관계를 파악

```python
sns.scatterplot(x='출생아수', y='혼인건수', hue='년도', data=df)
plt.show()
```

### pairplot 
+ 데이터프레임을 인수로 받아 그리드(grid) 형태로 각 데이터 열의 조합에 대해 scatter plot

```python
sns.pairplot(data=df)
plt.show()
```

### heatmap
+ 데이터가 2차원이고 모든 값이 카테고리 값

```python
sns.heatmap(df.corr(), annot=True)
plt.show()
```