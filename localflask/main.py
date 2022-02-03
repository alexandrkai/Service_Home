from flask import Flask, jsonify

def create_app(test_config=None):
    from API.routes import blueprint_api
    from CLI.routes import blueprint_cli
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.register_blueprint(blueprint_cli, url_prefix="/cli")
    app.register_blueprint(blueprint_api, url_prefix="/api")
    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route("/index")
    def index():
        app.logger.info('Запрос к index')
        return jsonify([
            {"response": app.config['HELLO_MESSAGE']},
            {"db_path": app.config['DATABASE_URL']}
        ])

    return app

if __name__ == "__main__":
    app = create_app()
    app.logger.info('Старт приложения')
    app.run(debug=True, host="0.0.0.0")
