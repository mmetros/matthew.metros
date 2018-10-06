from flask import flask
import sqlite3
from flask_migrate import Migrate

app = Flask(__name__)

@app.route('/')
def index():
    return null


if __name__ == "__main__":
    app.run(port=5000, debug=True)
