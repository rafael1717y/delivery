from flask import Flask

def red(filename):
    return [req.strip() for req in open(filename).readlines()]


def create_app():
    app = Flask(__name__)
    return app
    