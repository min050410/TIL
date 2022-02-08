# cpp11 auto, auto&, const auto& 

auto란 초기화 값에 따라서 타입을 추론해서 결정해주는 키워드다

auto a = 1;
printf("%d", sizeof(a))

결과 : 4

int 형을 추론 한다.

### range based for
```cpp
int main()
{
    list<Person> pl;
    Person p1("jeun",28);
    Person p2("jjeun",27);
    Person p3("jjjeun",26);
    Person p4("jjjjeun",25);
    Person p5("jjjjjeun",24);
    
    pl.push_back(p1);
    pl.push_back(p2);
    pl.push_back(p3);
    pl.push_back(p4);
    pl.push_back(p5);
    
    for(list<Person>::iterator iter = p1.begin(); iter!=p1.end(); iter++){
        printf("%s %d\n", (*iter).getName().c_str(),(*iter).getAge());
    }
}

// c_str() 함수는 string클래스로 변환하는 함수이다.
```

원래는 이런 식의 이터레이션을 쓰지만
auto range based for 를 쓰면 정말 편해진다.

```cpp
int main()
{
    list<Person> pl;
    Person p1("jeun",28);
    Person p2("jjeun",27);
    Person p3("jjjeun",26);
    Person p4("jjjjeun",25);
    Person p5("jjjjjeun",24);
    
    pl.push_back(p1);
    pl.push_back(p2);
    pl.push_back(p3);
    pl.push_back(p4);
    pl.push_back(p5);
    
    for(auto p:pl)
    {
        printf("%s %d\n",p.getName().c_str(),p.getAge());
    }
}


```

여기서 auto는 Person 타입이 된다.  
하지만 이렇게 하면 주소값이 다르게 나오는데, 로컬 변수 p로 복사가 된다. 

단순히 read만 하는건데 할 때마다 복사한다면 메모리 낭비가 있기 때문에
```cpp
auto &p : pl
```
이렇게 사용하는 것을 추천한다.

마지막으로 조심할 점은 값이 의도치 않게 변경될 수 있으니 상수화를 시킨 for(const auto &p:pl)이 베스트이다.


