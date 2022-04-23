from flask import Flask

app = Flask(__name__)
from flask import render_template


def main():
    app.run(port=8080, host='127.0.0.1')


@app.route('/')
def home_page():
    """начальная страница"""
    return render_template('index.html', title='Главная страница страница')


if __name__ == '__main__':
    main()
