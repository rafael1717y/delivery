def init_app(app):
    app.config['SECRET_KEY'] = "ahahdjfh19"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///delivery.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #app.config['DEBUG'] = True

    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True