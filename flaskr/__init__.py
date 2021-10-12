import os

from flask import Flask

def create_app(test_config=None):
    #Das hier ist die sogenannte Application Factory. Alle Settings etc der Anwendungen werden hier eingestellt / initialisiert.
    #Besserer Stil als globale Flask Instanz
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )



    if test_config is None:
        #lade die Konfigurationsinstanz, falls sie existiert und nicht getestet wird
        app.config.from_pyfile('config.py', silent=True)
    else:
        #lade die Testkonfiguration, falls diese übermittelt wird. Sinnvoll, da so die Tests später Konfigurationen unabhängig vom Deployment nutzen können
        app.config.from_mapping(test_config)

    #Stelle sicher, dass der Instanzen-Ordner existiert
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #URL die nur Hello World printed
    @app.route('/hello')
    def hello():
        return 'Hello World'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app