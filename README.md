# Learn_Flask
#개발시에 시간이 오래 걸렸거나 헷갈렸던 것들 모임  
#1  
GET은 서버의 리소스에서 데이터를 요청할 때, POST는 서버의 리소스를 새로 생성하거나 업데이트할 때 사용한다.  
DB로 따지면 GET은 SELECT 에 가깝고, POST는 Create 에 가깝다고 보면 된다.

#2  
html or css href 안에(이미지 파일참조 모두 포함)  
href = "{{url_for('static', filename='main.css')}}"

#3  
export FLASK_APP=\_\_init\_\_  
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
  
  
#5

def detail(post_id): #매개변수에는 <int:post_id>가 들어감  
	post = Post.query.get_or_404(post_id)  
	return render_template('post_detail.html', post=post)  
  
보면 detail의 매개 변수에는 post_id이다.  
templetes 에서 블루프린트 detail을 참조할 때,  
post_id=post.id로 들어가야 한다 (왼쪽이 매개변수 오른쪽이 db)  
아, 또 블루프린트를 참조할 때 * 꿀팁 *  
-> url_for('main.detail') main은 blueprint 이름, detail은 blueprint 함수 이름

#6  
플라스크 폼 모듈을 사용할 때  
Secret_key 무조건 필요    
config.py 에 정의 해야 한다.  
_+폼 모듈 너무 좋아요_

#7  
이 문제에 삽질한 횟수  
![image](https://user-images.githubusercontent.com/45661217/134806966-9ee02c84-74f4-4b6d-aed4-46daea631f67.png)  
gunicorn 을 사용할 때 모듈 네임드 에러가 계속 발생했었다.  
flask run 사용시 잘 되었지만  
gunicorn을 사용할 때만 모듈 상대 참조 오류가 계속 일어났다.    
gunicorn --bind 0:8080 "zelda:create_app()"  
__init__:create_app() 이 아닌 그 상위 디렉토리인 zelda로 설정해 줘야  
정상적인 참조가 가능하다.  

