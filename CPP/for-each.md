# cpp 반복문 / for_each 

for_each 자바에만 있는줄 알았는데 c++ 11부터 있었다고 한다.

### 근본 for

```cpp
for (int i=0; i<10; i++){
    cout << i;
}
```

### cpp11 부터 추가된 for
```cpp
for(int i: {0,1,2,3,4,5})
{
    cout << i;
}

vector<string> v;
for(const auto& element : v){
    cout << element;
}
```

index(i)가 안보여 귀찮게 느껴질 수도 있는데, while문 쓸 때처럼 반복문 밖에 변수를 선언하고 가져다 쓰면 된다.

깔끔해 보이는게 가장 큰 장점. 성능이 더 좋고 그런건 없다.

