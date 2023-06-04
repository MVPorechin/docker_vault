import os
from flask import Flask, jsonify, make_response


APP = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000
SERVICE_NAME = os.environ.get('SERVICE_NAME', 'application')
SERVICE_CONTACT = os.environ.get('USERNAME')

@APP.route('/hello/<user>')
def hello_user(user: str):
    return make_response(
        jsonify(
            {'message': f'Hello from {SERVICE_NAME},{user}!\n'
                        f'Support {SERVICE_CONTACT}'}
        ),
        200
    )


if __name__ == '__main__':
    APP.run(host=HOST, port=PORT)
