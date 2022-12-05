from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

from app import routes,models

if __name__ == "__main__":
    app.run()