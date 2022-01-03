# Flask 애플리케이션 환경변수 설정하기

> 우분투 환경입니다.

`.bash` 파일에 들어가 마지막 줄에 추가
```bash  
export FLASK_APP=__init__  
export FLASK_ENV=development  
```
재실행해야 환경변수가 저장됨

> window 환경에서는 `export` 가 `set` 이다. 참고!!  

- `.bash` 파일에서 환경변수를 이렇게 설정하면  
`flask run`을 쓸수 있고 애플리케이션 환경에서 개발이 가능하다.
```ubuntu
flask run --host=0.0.0.0 --port=8000
```