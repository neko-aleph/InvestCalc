from flask import Flask
from urls import urls_blueprint

app: Flask = Flask(__name__)
app.register_blueprint(urls_blueprint)

if __name__ == '__main__':
    app.run()
