# cpp lower_bound, upper_bound

### lower_bound, upper_bound 란? 
- 이진탐색으로 원소를 탐색해 배열 몇번째에서 처음 등장하는지 찾는 함수이다.

> 직접 구현할 필요 없이 cpp 에서 제공하고 있다.

시간복잡도는 이진탐색이니 O(logN) 이다.   
O(logN)을 무조건 사용해야만 하는 문제를 풀 때 유용하다.

lower_bound는 key 값과 같거나 큰 숫자를 반환하고  
upper_bound는 key 값을 초과하는 숫자를 반환한다.

### 사용법
```c
#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int arr[6] = {1,2,3,4,5,6};
    cout << "lower_bound(6)" << lower_bound(arr, arr+6, 6) - arr;
    return 0;
}
// 결과 -> 5
```

### 활용하기

> 5 이상 11 이하의 숫자 개수

```c
upper_bound(arr.begin(), arr.end(), 11) - lower_bound(arr.begin(), arr.end(), 5)
```

> 특정한 숫자가 몇번 나오는지 확인
```c
upper_bound(arr.begin(), arr.end(), 5) - lower_bound(arr.begin(), arr.end(), 5);
```