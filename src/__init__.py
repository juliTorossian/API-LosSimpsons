from flask import Flask

# Routes
from .routes import FraseRouter
from .routes import PersonajeRouter
from .routes import CapituloRouter

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(FraseRouter.main, url_prefix='/frase')
    app.register_blueprint(PersonajeRouter.main, url_prefix='/personaje')
    app.register_blueprint(CapituloRouter.main, url_prefix='/capitulo')

    return app