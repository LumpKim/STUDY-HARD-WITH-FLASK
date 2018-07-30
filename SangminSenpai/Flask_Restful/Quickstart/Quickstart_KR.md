Flask-RESTful Documentation Summary
===================================
## A Minimal API

- 'api.py'를 실행한 상태에서 **curl http://127.0.0.1:5000/** 를 실행해보자.
- **{"hello": "world"}** 라는 응답을 얻을 수 있다.

## Resourceful Routing
- 'api2.py'는 Flask-RESTful 라이브러리를 활용한 간단한 예제이다.
- 클래스를 선언하고, **add_resource(클래스 이름, '경로')** 를 이용하여 **@app.route('/', methods=[메소드 종류])** 를 대신할 수 있다.
- 클래스 내부에 선언된 함수의 이름은 메소드를 나타낸다.