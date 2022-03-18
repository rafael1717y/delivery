#from delivery.ext.site.main import bp
from .main import bp


# 2.Registra o blueprint

def init_app(app):
    app.register_blueprint(bp)
