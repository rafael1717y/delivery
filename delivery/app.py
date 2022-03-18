from flask import Flask
from delivery.ext import site

# 3. Inicia os blueprints

def create_app():
    app = Flask(__name__)
    site.init_app(app)
    return app







