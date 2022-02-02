from flask import Flask
import routes, cli
# from cli import bp
from db import conn
import log, logging

app = Flask(__name__)
app.logger.info('Старт приложения')
app.config.from_pyfile("config.py")
app.config['JSON_AS_ASCII'] = False # для кириллицы в конфиге
conn.init_app(app)

app.register_blueprint(cli.bp)
app.register_blueprint(routes.bp)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")