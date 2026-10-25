from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/api/teste')
    def teste():
        return {
            'message': 'API EletronicoShop funcionando!'
        }

    return app