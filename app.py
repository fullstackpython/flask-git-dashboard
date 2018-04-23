from flask import Flask, render_template, send_from_directory
from redis import Redis, RedisError
import os
import socket


# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__, static_url_path='/static')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route("/")
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8010, debug=True)
