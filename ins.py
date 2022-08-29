from datetime import timedelta
from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify("Hello world")
# @app.route('/example')
# def example():
#     return "some html page"
@app.route('/example1')
def example1():
    answer = "calling the backend to get the result"
    return answer

@app.route('/example2')
def example2():
    return jsonify("example2")

@app.route('/example3')
def example3():
    return jsonify("example3")
   
@app.route('/example4')
def example4():
    return jsonify("example4")


if __name__ == '__main__':
    app.run(debug=True)