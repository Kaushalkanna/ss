from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def message():
    return '<H1>Welcome to Smart System home page</H1>'


@app.route('/post-data')
def get_data():
    name = request.args.get('deviceName', default="None", type=str)
    val = request.args.get('value', default="None", type=str)
    return '{}: {}'.format(name, val)


if __name__ == '__main__':
    app.run()
