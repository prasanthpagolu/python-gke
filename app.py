import os

from flask import Flask, request
from calculator import add, subtract

app = Flask(__name__)


@app.route('/health')
def health():
    return 'Ok'


def servedByString():
    podName = os.environ.get('MY_POD_NAME', 'pod name')
    podIp = os.environ.get('MY_POD_IP', 'pod ip')
    return 'Served By Pod name {}, Pod Ip {}'.format(podName, podIp)


@app.route('/add')
def add_route():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    result = add(param1, param2)
    return result + '\n' + servedByString


@app.route('/subtract')
def sub_route():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    result = subtract(param1, param2)
    return result + '\n' + servedByString


@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
