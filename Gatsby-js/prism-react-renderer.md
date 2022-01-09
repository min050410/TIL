# Syntax highlighting 적용하기

> 개발을 하다 `mdx`를 불러오고 `syntax highlighting`이 적용 안되는 것을 발견했다. 

`syntax highlighting` 이란 이것이다
```js
const youngmin = () =>{
    if(이렇게){
        var 색깔이 = 바뀌는게
        문법 하이라이팅이다.
    }
} 
```

[공식 문서](https://www.npmjs.com/package/prism-react-renderer)를 따라하며 적용해보자

`prism-react-renderer` 패키지를 받자
```shell
npm install prism-react-renderer
```

그리고 공식 문서의 `CodeBlock` 컴포넌트를 가져온다. 컴포넌트를 새로 만들어서 내용을 넣는다.
```js
import React from "react";
import { render } from "react-dom";
import Highlight, { defaultProps } from "prism-react-renderer";

const exampleCode = `
(function someDemo() {
  var test = "Hello World!";
  console.log(test);
})();

return () => <App />;
`;

render((
  <Highlight {...defaultProps} code={exampleCode} language="jsx">
    {({ className, style, tokens, getLineProps, getTokenProps }) => (
      <pre className={className} style={style}>
        {tokens.map((line, i) => (
          <div {...getLineProps({ line, key: i })}>
            {line.map((token, key) => (
              <span {...getTokenProps({ token, key })} />
            ))}
          </div>
        ))}
      </pre>
    )}
  </Highlight>,
  document.getElementById('root')
);
```

그리고 스타일을 적용하고 싶은 곳에 `@mdx-js/react`의 `MDXProvider` 컴포넌트에 `components prop`으로 넘겨주면 끝이다.

```js
import { MDXProvider } from "@mdx-js/react"
import CodeBlock from "../components/CodeBlock";
...

const components = { //코드 스타일링
  code: CodeBlock,
};

const PostTemplate = () => {
    ...
    <MDXProvider components={components}>
        //Syntax Highlight 적용될 부분
    </MDXProvider>
    ...
}
```
