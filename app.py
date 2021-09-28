from flask import Flask, render_template

app = Flask(__name__)


def create_app():
    @app.route("/")
    def home():
        return render_template('index.html')
    return app
