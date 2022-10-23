from flask import Flask

app = Flask(__name__)


def suma(a, b):
    return a + b

# caracteristica creada


@app.route('/')
def index():
    return "Hello world"
