from flask import jsonify

from main import app


@app.route("/")
def index():
    app.logger.info('Запрос к index')
    return jsonify([
        {"response": app.config['HELLO_MESSAGE']},
        {"db_path": app.config['DATABASE_URL']}
    ])
