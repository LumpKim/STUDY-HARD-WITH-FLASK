RESTful Summary
===============
- http://blog.sonim1.com/105를 참고함

## REST가 무엇일까요
- **REpresentational State Transfer**의 약자
- 장비 간 통신을 위해 HTTP를 이용
- 자원 지향 구조로 구성, 모든 자원에 고유한 URI 부여
- 로이 필딩의 박사학위 논문에서 소개됨
- 네트워크 아키텍처 원리: 자원을 정의하고 자원에 대한 주소를 지정하는 방법

## CRUD는 또 뭘까요?
- **Create Read Update Delete** 의 약자

| CRUD |역할|  REST |
|------|----|-------|
|Create|생성|  POST |
| Read |조회|  Get  |
|Update|수정|  Put  |
|Delete|삭제|Delete |
- URL이 같더라도 메소드가 다르면 하는 역할도 달라진다.

## URL은 동사 대신 명사 사용

- 메소드가 동사의 역할을 하기 때문에 URL에 동사를 붙이지 않아도 됨.
```angular2html
    GET /getUser/홍길동 → [X]
    GET /user/홍길동 → [O]
```

## 6가지 아키텍처 스타일
### Client-Server
- 여러 클라이언트서 하나의 REST API를 사용할 수 있음

|          |  역할                                 |
|----------|---------------------------------------|
| REST서버 |비즈니스 로직 처리 및 저장              |
|클라이언트|사용자 인증, 컨텍스트 등을 직접 관리/책임|

### Stateless(무상태성)
- 상태 정보를 저장하지 않고 API서버는 들어온 요청을 같이 들어온 메시지로만 처리
- 구현이 단순해짐(컨텍스트 정보 신경 X)

### Cache
- **Last-Modified** 태그나 **E-tag** 이용하면 구현 가능
- 응답시간, 성능, 서버의 자원 사용률 향상 가능

### Uniform Interface
- HTTP 표준을 따른다면 무엇이든 사용이 가능한 인터페이스 스타일임

### Layered System
- intermediary(매개자, 중개자) 서버 등을 통해서 확장성/보안성 확장 가능함

### Code-On-Demand(반드시 충족 필요 X)
- 서버로부터 스크립트를 받아 Client에서 실행하는 것
