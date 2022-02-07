# cpp vector

cpp stl의 sequence container 중 정말 자주 쓰는 vector에 대해서 알아보자

vector 컨테이너는 자동으로 메모리가 할당되는 배열이다.

모든 stl 이 template을 사용하듯 vector도 데이터 타입은 마음대로 넣을 수 있다.

stack과 비슷한 느낌이다. 맨 뒷쪽에서 삽입과 삭제가 가능하다.

### vector의 사용
- vector header file 추가
- using namespace std; 를 해주면 편리
vector의 선언은 vector <[datatype]> [변수이름] 이다.
```cpp
// ex
vector<int> v;
```
### vector의 생성자와 연산자
### vector<int> v;    
vector v 생성  
### vector<int> v(5);  
기본값으로 초기화 된 5개의 원소를 가지는 vector v 생성  
### vector<int> v(5, 2);  
2로 초기화 된 5개의 원소를 가지는 vector v 생성  
### vector<int> v2(v1);  
v2 는 v1을 copy 하여 생성

### vector의 멤버 함수
v.assign(5,2)
- 2의 값으로 5개의 원소 할당

v.at[idx];
- idx 번째 원소를 참조

v[idx];
- idx 번째 원소를 참조
- 속도가 가장 빠르지만 범위를 점검하지 않음

v.front();
- 첫번째 원소 참조

v.back();
- 마지막 원소 참조

v.clear();
- 모든 원소 제거
- 원소만 제거하고 메모리는 남아있음

v.push_back(7);
- 마지막 원소 뒤에 원소 7을 삽입함

v.pop_back();
- 마지막 원소를 제거

v.begin();
- 첫번째 원소 가리키기

v.end();
- 마지막의 다음 가리키기

v.rbegin();
- begin의 reverse버전

v.reserve(n);
- n개의 원소를 저장할 위치를 예약

v.resize(n);
- 크기 변경

v.resize(n,3)
- 더 커졌을 경우 인자의 값을 3으로 초기화

v.size();
- 원소의 개수 리턴

v.capacity();
- 할당 공간의 크기 리턴(기존 메모리 * 2로 증가)

v2.swap(v1);
- v1과 v2의 원소와 capacity 를 바꿔준다. (모든걸 스왑해줌)

v.insert(2,3,4);
- 2번째 위치에 3개의 4값 삽입

v.erase(iter);
- iter가 가리키는 원소를 제거

v.empty();
- vector가 비었으면 리턴 true

### iterator 지정법
> 반복자(iterator)는 객체 지향적 프로그래밍에서 배열이나 그와 유사한 자료 구조의 내부의 요소를 순회(traversing)하는 객체이다.

```cpp
vector<int>::iterator iter;
// 값을 참조할 때는 *iter로 사용
// 포인터 변수와 비슷함
```

### 다양한 접근 방법 및 출력

```cpp
#include<iostream>
#include<vector>
using namespace std;
 
int main(void){
    vector<int> v;
    
    v.push_back(21);
    v.push_back(32);
    v.push_back(53);
    v.push_back(64);
    v.push_back(15);
    
    
    //ex1) 멤버형식 size_type 이용한 반복.
    cout << "ex1-1) [v.at(i)] size_type : " ;
    for(vector<int>::size_type i =0; i<v.size(); i++){
        cout << v.at(i) << " ";
    }
    cout << endl;
    cout << "ex1-1) [ v[i] ] size_type : " ;
    for(vector<int>::size_type i =0; i<v.size(); i++){
        cout << v[i] << " ";
    }
    cout << endl << endl;
    
    
    //ex2) int i 를 이용한 반복.
    cout << "ex2-1) [v.at(i)] int : " ;
    for(int i =0; i<v.size() ; i++){
        cout << v.at(i) << " ";
    }
    cout << endl;
    cout << "ex2-2) [ v[i] ] int : " ;
    for(int i =0; i<v.size() ; i++){
        cout << v[i] << " ";
    }
    cout << endl << endl;
    
    
    //ex3) 반복자 iterator를 이용한 반복. 
    cout << "ex3) [*iter] iterator : ";
    vector<int>::iterator iter;
    for(iter = v.begin(); iter != v.end() ; iter++){
        cout << *iter << " ";
    }
    cout << endl << endl;
    
 
    return 0;
}


출처: https://blockdmask.tistory.com/70 [개발자 지망생]
```
