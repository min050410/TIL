# TIL
react-native today I learned 

#1. 컴포넌트 안에 기본적으로 나뉘는 js 파일들을 집어넣는다.  
|- components    
&nbsp;&nbsp;&nbsp;&nbsp;  |-TodoInsert.js  
&nbsp;&nbsp;&nbsp;&nbsp;  |-TodoList.js  
&nbsp;&nbsp;&nbsp;&nbsp;  |-TodoListItem.js  
(like this)  
  
#2. 훅 문법은 const App = () => {  
안에 넣는다   
ex) const [todos, setTodos] = useState([]);  
  
#3. 모듈이 동작하지 않을때  
$ npm install <module-name> --save  
  
출처: https://xtring-dev.tistory.com/11 [xtring.dev]  

#4. 컴포넌트 분리 방법과 하는 법  
컴포넌트 파일 내에 엡 작성 + export default  
그 후 그 파일을 임포트, 파이썬 모듈 불러오는것과 비슷  
 ex ) import TodoInsert from './components/TodoInsert';
