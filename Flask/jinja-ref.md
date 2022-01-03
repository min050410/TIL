# Jinja에서 이미지나 파일 불러오기

Jinja에서는 url_for를 이용해서 파일을 불러올 수 있다. 

```html
href = "{{url_for('static', filename='main.css')}}"
```