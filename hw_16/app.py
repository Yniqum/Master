from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route('/user')
def user():
    return "Меня зовут Дмитрий"


if __name__ == "__main__":
    app.run(debug=True)
