# TIL
> react-native today I learned 
### react-native 코드 보기
- <a href="https://github.com/min050410/RN_practice/tree/master">Simple Todo App</a>
- <a href="https://github.com/min050410/RN_practice/tree/navigation">Navigation Practice</a>
- <a href="https://github.com/min050410/NOTIFAM">NOTIFAM</a>
> #1
- `components` 안에 기본적으로 나뉘는 js 파일들을 집어넣는다.  
* `components`    
  * `TodoInsert.js ` 
  * `TodoList.js` 
  * `TodoListItem.js`

(like this)  
  
> #2
- 훅 문법은 const App = () => {  
안에 넣는다   
```js
const [todos, setTodos] = useState([]);  
```
> #3 
- `node_modules`가 동작하지 않을때  
```terminal
$ npm install <module-name> --save  
```
출처: `https://xtring-dev.tistory.com/11`

> #4

`component` 분리 방법과 하는 법  
원래 #1 앞에 적었어야 했는데 후에 적음  
컴포넌트 파일 내에 앱 작성 + `export default`   
그 후 그 파일을 `import`, 파이썬 모듈 불러오는것과 비슷
```js
import TodoInsert from './components/TodoInsert';
```
