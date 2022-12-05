from flask import Flask
from .config import Config
from flask_bootstrap import Bootstrap
from .routes.personajes import personajes_ruta

def create_app(): #fx de fabrica
    app=Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    
    app.register_blueprint(personajes_ruta)
    
    return app