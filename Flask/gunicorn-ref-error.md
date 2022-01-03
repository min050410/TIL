# Gunicorn 참조 에러 ❌
 
이 문제에 삽질한 횟수  

![image](https://user-images.githubusercontent.com/45661217/134806966-9ee02c84-74f4-4b6d-aed4-46daea631f67.png) 
  
`gunicorn` 을 사용할 때 모듈 네임드 에러가 계속 발생했었다.  
`flask run` 사용시 잘 되었지만  
`gunicorn`을 사용할 때만 모듈 상대 참조 오류가 계속 일어났다.    

```ubuntu
gunicorn --bind 0:8080 "zelda:create_app()"  
```

`__init__ :create_app()` 이 아닌 그 상위 디렉토리인 zelda로 설정해 줘야  
정상적인 참조가 가능하다. `gunicorn`은 `flask run`과 다르게 한 단계 상위에서 실행해줘야 하는 것 같다.  
또, 디렉토리가   
`ch01`
    \- `zelda` 
        \- `__init__` 이런 배치로 있다면    
`flask run` 과 달리 상위 디렉토리 `ch01`에서 명령어를 입력해야 한다.

> 초보적인 실수지만 참조 오류는 뼈아프다는걸 깨달았다.. ㅠㅠ  

> 2022/1/3 - 4개월 전인가? 파일하나하나 바꾸고 진짜 힘들었는데
