from flask import Flask, request

app = Flask(__name__)

user = []
logged_in = False


@app.route('/')
def index():
    return "Jaehoon's Index Page"


@app.route('/signup', methods=['POST'])
def signup():
    user.append(request.json)
    return '회원가입 완료', 200


@app.route('/login', methods=['POST'])
def login():
    email = user.append(request.json['email'])
    password = user.append(request.json['password'])

    for u in user:
        if email == u['email']:
            if password == u['password']:
                return u['name'] + '님 정상적으로 로그인 되었습니다.', 200
        else:
            return '잘못된 접근입니다.', 204


if __name__ == '__main__':
    app.run()
