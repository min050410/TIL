# Learn_Flask
#개발시에 시간이 오래 걸렸거나 헷갈렸던 것들 모임  
#1  
* GET은 서버의 리소스에서 데이터를 요청할 때, POST는 서버의 리소스를 새로 생성하거나 업데이트할 때 사용한다.  
* DB로 따지면 GET은 SELECT 에 가깝고, POST는 Create 에 가깝다고 보면 된다.

#2  
html or css href 안에(이미지 파일참조 모두 포함)  
href = "{{url_for('static', filename='main.css')}}"

#3  
export FLASK_APP=__init__  
export FLASK_ENV=development  
우분투 환경에서는 set 이 export 이다. 참고!!  
"flask run을 쓸수 있고 애플리케이션 환경에서 개발 가능하다."  
  
flask run --host=0.0.0.0 --port=8000

#4  

__*"역시 믿고보는 stackoverflow"*__  
flask db stamp head 현재 리비전을 최종 리비전으로 변경하는 명령어  
flask db migrate  
flask db upgrade  
  
flask db upgrade를 꼭 해야만 db.session.commit()이 가능해진다 
