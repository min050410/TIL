# 비동기에서 동기로 코드 짜는법

### 📑useEffect 사용
`react native` `hook Usestate` 는 비동기이다.
```js
//3으로 생각하기 쉽지만 비동기 이기 때문에 마지막 함수만 실행됨
setIsloding(isloding+1);
setIsloding(isloding+1);
setIsloding(isloding+1);
```

- 간단하게 `동기`로 만드는 법
```js
//app.js
//useEffect 사용예시
const App = () => {
/...
useEffect(() => {
    goPhoto();
  }, [uploadData]);
/...
setuploadData(nowdata);
/...
}
export default App;
```

이렇게 하면 `uploadData`가 올라왔을때 `goPhoto()` 라는 함수가 실행된다  
그리고 `useEffect`를 `import` 하는걸 잊지 말자

```js
import {useState, useEffect} from 'react';
```