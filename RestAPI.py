from flask import Flask, request
import os
import redis

app = Flask(__name__)


@app.route('/')
def message():
    r = redis.from_url(os.environ.get("REDIS_URL"))
    return '<H1>Welcome to Smart System home page</H1><H3>{}</H3>'.format(r)

@app.route('/post-data')
def post_data():
    name = request.args.get('deviceName', default="None", type=str)
    val = request.args.get('value', default="None", type=str)
    return '{}: {}'.format(name, val)


@app.route('/get-data')
def get_data():
    return 'Nothing to return yet!!'


if __name__ == '__main__':
    app.run()
