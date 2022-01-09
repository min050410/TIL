# Gatsby란?

`Gatsby` 는 `JAM Stack` 을 활용한 정적 사이트 생성기다.

> JAM Stack 은 JavaScript, API, MarkUp Stack 의 약자로, 
JavaScript 와 API, HTML 이나 CSS 등을 칭하는 MarkUp 으로 이루어진 웹 구성 방법이다.

### 📑 JAM Stack의 동작원리
기존 웹 사이트의 방식은 대부분 서버의 데이터베이스 또는 CMS(Content Management System)에서 추출한 데이터를 프론트에 뿌려주는 방식이다.

클라이언트에 데이터를 보여주기 위해 많은 절차를 거쳐야 해서 대부분 구조가 복잡하다.  

하지만 Jam Stack의 방식을 기존 웹사이트와 다르게 간단하다.  
![pre-renderer](https://www.bottlehs.com/assets/jamstack-advantage-2.png)  
Jam Stack은 렌더링할 화면들을 모두 `Pre-Render` 하여 제공해서 그만큼 사용자에게 화면을 보여주기 위해 준비하는 시간을 단축할 수 있다.

![safe](https://www.bottlehs.com/assets/jamstack-advantage-1.png)  
Jam stack은 사진처럼 API를 통해 정적 사이트를 생성하는데  
여기서 사용되는 API는 각 프레임워크의 마이크로 서비스로써, 사이트 생성을 위한 프로세스가 추상화 되어 있어 그만큼 공격 노출 번위가 감소하게 된다.

### 📑 Next.js vs Gatsby
|프레임워크|용도|
|--|--|
`Next.js`| 주로 서버 사이드 렌더링을 위해 쓰임
`gatsby.js`| 서버 없이, 오로지 정적 사이트 생성을 위해 사용

그래서 `gatsby.js`는 소개, 블로그, 포트폴리오에 많이 사용된다.



