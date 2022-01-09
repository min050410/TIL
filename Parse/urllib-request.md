# urllib request로 api 파싱하기

# urllib.request 모듈
+ URL과 웹 요청에 관련된 모듈들 패키지로 묶어 제공한다
* 웹 페이지 요청 및 데이터를 가져올 수 있다

### urlopen(url, data)
* 웹 서버에 정보를 요청한 후, 돌려받은 응답을 저장하여 ‘**응답 객체(HTTPResponse)**’를 반환한다.
* data는 서버로 전송할 추가 데이터를 지정하는 객체이다
* 반환된 응답 객체:  `read()` 메서드를 실행
```python
resp.read().decode('utf-8')
```  

 ### urllib.request.Request(url, headers={})
* POST방식으로 데이터를 보내려고 할 경우 
  + URL : 요청 주소
  * headers : 딕셔너리형태의 헤더


