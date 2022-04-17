# cpp 생성자 

cpp 에서 생성자는 java와 문법이 같다.  

```
#include <iostream>
#include <algorithm>

using namespace std;

class Point
{
private:
    float x, y;
public:
    // 생성자 
    Point(const float& xpos, const float& ypos){ x=xpos; y=ypos;}
    float GetX() const { return x; }
    float GetY() const { return y; }
    void SetX(const float& xpos) { x = xpos; }
    void SetY(const float& ypos) { y = ypos; }
    void ShowPointInfo() const
    {
        cout << '[' << x << ", " << y << "]" << endl;
    }
};

class Circle
{
private:
    Point p;
    float r;
public:
    // 생성자
    Circle(const float& xpos, const float& ypos, const float& rlen) : p(xpos, ypos){
        r = rlen;
    }

    void ShowCircleInfo() const{
        p.ShowPointInfo();
        cout << "반지름 : " << r << endl;
    }
};
```

생성할 때는 자바와 같이 클래스 명과 같은 이름으로 생성자를 만들고,   
멤버 변수의 클래스를 바로 생성할 때에는  
`:` 콜론을 사용하여 생성자 뒤에 붙여 생성한다.  

