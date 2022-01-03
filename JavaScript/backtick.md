# Backtick 부호 문법

- `JavaScript` backtick syntax => \`  
`JavaScript` 억음 부호 문법

python 의 `f string` 처럼 사용 가능  
사용 예시
```ts
//기존의 js 문법
const welcome = 'You have logged in as ' + first + ' ' + last + '.'

const db = 'http://' + host + ':' + port + '/' + database;
```
```ts
//backtick 문법
const welcome = `You have logged in as ${first} ${last}`;

const db = `http://${host}:${port}/${database}`;
```