# Flask로 Blueprint에서 다른 url에 값 주기

```python
def detail(post_id): #매개변수에는 <int:post_id>가 들어감  
	post = Post.query.get_or_404(post_id)  
	return render_template('post_detail.html', post=post)  
```

- `detail`함수의 매개 변수에는 `post_id`이다.  
블루프린트 `detail`을 참조할 때,  
`post_id=post.id`의 형태로 작성해야 한다 (왼쪽이 `매개변수` 오른쪽이 `db`)  

### 📑html 파일에서 blueprint 참조하기 (번외) 
`url_for('main.detail')` main은 blueprint 이름, detail은 blueprint 함수 이름으로 참조한다.