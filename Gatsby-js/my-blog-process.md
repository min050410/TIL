# 블로그 제작기 - Devlog

> `markdown` 으로 빠르게 편집 가능하고  
> `TIL`에 쓴 내용을 블로그에 빠르게 적용이 가능하고  
> 정적인 블로그 제작을 원했다.

![gatsby](https://theme.zdassets.com/theme_assets/9381034/684b20f7da44f0965a32f1a13222f5e587b04eca.png)  

그렇게 찾다 보니 `Gatsby` 라는 `react` 기반의 프레임워크를 찾았다  
`react`기반이라 경험을 살려 `typescript`로 개발을 시작하고 블로그는 1주일 후에 모습을 드러내게 되었다.  

직접 개발한 블로그의 장점들을 소개하겠다

### 👉 url query 형식으로 유동적인 Blog 관리가 가능하다
```
https://devlog.kro.kr/postitem?name=ohmyposh
```
이렇게 `name query`에 `ohmyposh` 라는 파일 명을 받아와 
`ohmyposh.md` 를 랜더링하는 식으로 제작했다.

### 👉 블로그의 모든 정보들을 배열에 저장해 빠른 참조가 가능하다
```ts
{
    id: 1,
    title: 'Big-O 표기법과 수행',
    filename: 'Algorithm',
    img: 'algorithm',
    date: '2021-12-20',
    tag: 'Big O',
    tag2: 'sort',
    tag3: 'DP',
    filter: 'c'
},
```
이렇게 정보들이 배열로 저장되어 있어 참조하기도 쉽고 정보를 수정하기도 용이하다.

### 👉 `markdown`으로 작성하면 알아서 `blog`의 테마에 맞게 알아서 변환해준다.

`gatsby-plugin-mdx` plugin을 사용하고 `style`에 손을 좀 봐서 가능해졌다.  
`react-prism-renderer`를 이용해 `markdown`의 `syntax highlighting`을 적용했다.

### 👉 자체 cloud가 무료이다

첫 `app`은 무료였다. 여기서 자세한 정보를 볼 수 있다.  
[gatsby cloud](https://www.gatsbyjs.com/products/cloud/)








