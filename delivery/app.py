from flask import Flask
from delivery.ext import site
from waitress import serve

# 3. Inicia os blueprints

def create_app():
    app = Flask(__name__)
    site.init_app(app)
    serve(app, host='0.0.0.0', port=5000)
    return app







