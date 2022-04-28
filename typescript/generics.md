# 제네릭(Generics)

제네릭이란 타입을 마치 함수의 파라미터처럼 사용하는 것이다.

```ts
function getText(text) {
    return text;
}
```

위 함수는 text라는 파라미터에 값을 넘겨 받아 text를 반환해준다.

```ts
// (text: T) 매개변수의 타입
// :T return 값의 타입
function getText<T>(text: T): T {
    return text;
}

// 함수 호출 시 
getText<string>('hi');
getText<number>(10);
getText<boolean>(true);
```



