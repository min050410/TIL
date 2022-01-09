# Sass 간략한 장점과 gatsby 적용방법

### 📑 내가 Sass를 쓰는 이유

`sass` 로
```scss
@include(header)
```
와 같은 문법으로 파일을 가져오거나
```scss
@mixin header
```
로 중복되는 스타일들을 하나로 묶을 수 있다.  
또, 변수를 쓸 수 있는 것도 엄청난 장점이다.   
가장 편한 것은 세미콜론을 안써도 된다는 것이다. 

### 📑 gatsby 적용법

1. `gatsby-plugin-sass` download
```shell
npm install sass gatsby-plugin-sass
```

2. `gatsby-plugin` include
```js
plugins: [`gatsby-plugin-sass`] //파일은 gatsby-config.js
```
