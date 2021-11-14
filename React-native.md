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

> #5

`react native`로 쉽게 `API xml` 파싱하는법  
먼저,   
```terminal
npm install xml2js
```
`xml2js`를 다운한다.  
필자의 경우는 `string` 을 `xml`로 옮길 것이므로  
```js
import { parseString } from 'xml2js';
```
`parseString` 만 임포트 한다 
```js
parseString(text, function (err, result) {
                // console.log(result['lists']['list'][0]['PUM_NM_A']);
                setData(result['lists']['list'][0]['PUM_NM_A']);
                setPrice(result['lists']['list'][0]['AV_P_A']);
                setWeight(result['lists']['list'][0]['U_NAME']);
            })
```
그 후 이렇게 `parseString` 메서드를 이용해 `xml`로 파싱하고 값을 정상적으로 참조할 수 있다  

`xml2js`를 객체로 쓰고싶은 사람은
```js
var xml2js = require('xml2js');
var parser = new xml2js.Parser();
var fs = require('fs');
 
var xml = fs.readFileSync(__dirname + '/user.xml', 'utf-8');
 
parser.parseString(xml, function(err, result) {
  console.log(result);
});
```
이런 식으로 가능하다
  
아 그리고 __꿀팁__    
`react native`에서의 `console.log`는 `metro`에서 나온다 참고


