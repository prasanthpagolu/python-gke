import os

from flask import Flask, request
import calculator

app = Flask(__name__)


@app.route('/health')
def health():
    return 'Ok'


def get_service_host():
    service_host = os.environ.get('CALCULATOR_SERVICE_HOST', 'service host')
    return '<br/>Served By service host {}'.format(service_host)


@app.route('/add')
def add():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    result = calculator.calculate("ADD", param1, param2)
    return str(result) + get_service_host()


@app.route('/subtract')
def sub():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    result = calculator.calculate("SUBTRACT", param1, param2)
    return str(result) + get_service_host()


@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
