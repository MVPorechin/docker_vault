import os
from flask import Flask, jsonify, make_response


APP = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000
SERVICE_NAME = os.environ.get('SERVICE_NAME', 'application')


@APP.route('/hello/<user>')
def hello_user(user: str):
    return make_response(
        jsonify(
            {'message': f'Hello from {SERVICE_NAME}, {user}!'}
        ),
        200
    )


if __name__ == '__main__':
    """
    sudo docker container run -p5050:5000 -e "SERVICE_NAME=serviceХ" flask_app:v0.1
    -p5050:5000 - это аргумент принимает 2 числа разделеный :
    5050 - порт для использования хоста для связи с портом внутри контейнера
    5000 - на какой порт внутри контейнера перенаправлять запросы порта хоста
    -e "SERVICE_NAME=service1" - передаем в окружение переменную с именем сервиса
    serviceХ - имя нашего сервиса, где Х- любое число или имя 
    """
    APP.run(host=HOST, port=PORT)
