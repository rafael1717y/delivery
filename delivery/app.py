from flask import Flask

from delivery.ext import site
from delivery.ext import config
from delivery.ext import toolbar
from delivery.ext import db
from delivery.ext import migrate
from delivery.ext import cli
from delivery.ext import hooks
from delivery.ext import auth
from delivery.ext import admin

# 3. Inicia os blueprints

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)
    admin.init_app(app) # inicializar depois da autenticação
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app) 
    hooks.init_app(app)   
    return app

