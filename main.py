# Автор: Alena Melnikova
from flask import Flask, request, jsonify
import json
from utils import memoized, save_cache, load_cache

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def author():
    return "<p>Alena Melnikova</p>"

@app.route("/calc/<string:func>/<int:number>")
def calculate(func, number):
    if func == 'f1':
        res = f'factorial of {number} = {factorial1(number)}'
    elif func == 'f2':
        res = f'factorial with scipy of {number} = {factorial2(number)}'
    else:
        res = 'other function'
    return res

@app.route("/save_to_cache", methods=["GET"])
def save_cache_route():
    cache = factorial1.cache
    save_cache(cache)
    return jsonify({"message": "Cache saved successfully"}), 200

@app.route("/load_from_cache", methods=["GET"])
def load_cache_route():
    cache = load_cache()
    factorial1.cache = cache
    return jsonify({"message": "Cache loaded successfully"}), 200

@memoized
def factorial1(n):
    from math import factorial
    return factorial(n)

@memoized
def factorial2(n):
    from scipy.special import factorial
    return factorial(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


