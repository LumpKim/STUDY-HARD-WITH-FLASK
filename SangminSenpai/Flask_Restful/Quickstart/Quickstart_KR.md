Flask-RESTful Documentation Summary
===================================
- https://flask-restful.readthedocs.io/en/latest/quickstart.html를 정리함
- http://na27.tistory.com/230 를 참고함
## A Minimal API

- 'api.py'를 실행한 상태에서 **curl http://127.0.0.1:5000/** 를 실행해 봅시다.
- **{"hello": "world"}** 라는 응답을 얻을 수 있습니다.

## Resourceful Routing
- 'api2.py'는 Flask-RESTful 라이브러리를 활용한 간단한 예제입니다.
- 클래스를 선언하고, **add_resource(클래스 이름, '경로')** 를 이용하여 **@app.route('/', methods=[메소드 종류])** 를 대신할 수 있습니다.
- 클래스 내부에 선언된 함수의 이름은 메소드를 나타냅니다.

## Endpoints
- API에서, 리소스는 여러 URL을 가집니다.
- **add_resource()** 메소드를 이용해 여러 URL을 하나로 일치시킬 수 있습니다.
```python
api.add_resource(HelloWorld,
    '/',
    '/hello')
```
- 경로의 일부분을 변수로 사용할 수 있습니다.
```python
api.add_resource(Todo,
    '/todo/<int:todo_id>', endpoint='todo_ep')
```

## Argument Parsing
- 플라스크는 Request Data에 대한 손쉬운 접근을 제공하지만, 폼 데이터를 검증하는 건 여전히 어려운 일입니다.
- 이에 Flask-RESTful에서는 argparse와 비슷한 라이브러리를 사용한 요청 데이터 확인(Request Data Validation) 기능이 내장되어 있습니다.
```python
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to charge for this resource')
args = parser.parse_args()
```
- 각주: argparse 모듈과는 달리, **reqparse.RequestParser.parse_args()** 는 Custom data structure(사용자 정의 데이터 구조?) 대신에 파이썬 딕셔너리를 반환합니다.
- **reqparse** 모듈을 사용하면 온건한 에러 메세지를 자유롭게 전달합니다.(의역)
- **inputs** 모듈은 inputs.date()와 inputs.url()과 같이 몇몇 내장된 공통의 변환 함수를 제공합니다.
- strict=True 로 parse_args 를 호출했을 때 구문 분석기로부터 정의되지 않은 인수가 요청에 포함된 경우 오류가 발생합니다.
```python
args = parser.parse_args(strict=True)
```

## Data Formatting
- Flask-RESTful에서는 **fields** 모듈과 **marshal_with** 데코레이터를 제공합니다. 이는 장고의 ORM과 WTForm과 비슷하며, fields 모듈을 사용하여 Response의 구조를 설명합니다.
```python
from flask_restful import fields, marshal_with

resource_fields = {
    'task':   fields.String,
    'uri':    fields.Url('todo_ep')
}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')
```
- 위의 예제에서는 파이썬 개체를 가져와 일련화할 준비를 합니다.
- **marshal_with()** 데코레이터는 **resource_fields**에서 기술하는 변환을 적용합니다.

## ETC...
- fullExample.py
- 파서랑 파싱이 뭘까요
    - 파싱(Parsing): 데이터를 조립해 원하는 데이터를 빼내는 프로그램을 하는 것
        - 컴퓨터 과학에서 일련의 문자열을 의미있는 token 으로 분해하고 그것들로 이루어진 Parse tree를 만드는 과정
        - 어떤 data를 내가 원하는 porm으로 만들어 내는 것
        - 프로그램을 컴파일 하는 과정에서 특정 프로그래밍 언어가 제시하는 문법을 잘 지켜서 작성하였는지 컴파일러가 검사하는 것