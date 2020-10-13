from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def _root():
    return "Hello World"


@app.route('/get/<username>', methods=['GET'])
def get(username):
    args = request.args
    return f"get:{username} args:{args}"


@app.route('/post', methods=['POST'])
def post():
    # args = request.args
    args = request.form
    return f"post {args}"


@app.route('/put', methods=['PUT'])
def put():
    args = request.form
    return f"put {args}"


if __name__ == '__main__':
    app.run()
