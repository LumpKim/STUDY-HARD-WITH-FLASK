# How to use Blueprints in Flask

플라스크의 확장 기능인 Flask-restful의 <code>api.add_resource()</code>를 사용하다보니 블루프린트의 필요성을 잘 느끼지 못했습니다. 하지만 파일 구조를 프로젝트 구조로 확장하다 보니 그 필요성을 느끼게 되었고, 공부하는 겸 이렇게 정리해 보았습니다.

## What is Blueprint?

블루프린트란, 모듈을 url에 등록하기 쉽게 해주는 방법입니다. 대부분 한 곳에 집중되어 있는 URL 매핑을 모듈로 분할시켜 작업의 생산성을 향상시키고, 나중에 이들을 한 곳에 모을 수 있도록 한 것이 바로 블루프린트라고 할 수 있죠.  

## Examples

