import os

from flask import Flask, request
import calculator

app = Flask(__name__)


@app.route('/health')
def health():
    return 'Ok'


def servedByString():
    podName = os.environ.get('POD_NAME', 'pod name')
    podIp = os.environ.get('POD_IP', 'pod ip')
    hostIp = os.environ.get('HOST_IP', 'host ip')
    return '\nServed By Pod name {}, Pod Ip {}, Host Ip {}'.format(podName, podIp, hostIp)


@app.route('/add')
def add():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    result = calculator.calculate("ADD", param1, param2)
    return str(result) + servedByString()


@app.route('/subtract')
def sub():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    result = calculator.calculate("SUBTRACT", param1, param2)
    return str(result) + servedByString()


@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
