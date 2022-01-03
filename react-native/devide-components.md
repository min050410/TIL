# react-native 컴포넌트 나누기

- `components` 안에 나뉘는 js 파일들을 집어넣는다. (사람마다 다름) 
* `components`    
  * `TodoInsert.js ` 
  * `TodoList.js` 
  * `TodoListItem.js`

### 📑 `component` 분리 방법과 하는 법  
컴포넌트 파일 내에 앱 작성 + `export default`   
그 후 그 파일을 `import`, 파이썬 모듈 불러오는것과 비슷하다  
```js
import TodoInsert from './components/TodoInsert';
```
