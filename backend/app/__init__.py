from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    from app.models import Produto  # Import the Produto model to register it with SQLAlchemy

    @app.route('/api/teste')
    def teste():
        return {
            'message': 'API EletronicoShop funcionando!'
        }

    return app