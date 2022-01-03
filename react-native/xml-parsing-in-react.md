# react native로 쉽게 API xml 파싱하는법  

먼저,   
```terminal
npm install xml2js
```

`xml2js`를 다운한다.  

나의 경우는 `string` 을 `xml`로 옮길 것이므로  
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