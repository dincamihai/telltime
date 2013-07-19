import flask
from datetime import datetime
from flask import Flask, render_template, request
from geobaza import GeobazaQuery

root = flask.Blueprint("index", __name__)

def initialize_app(app):
    app.register_blueprint(root)

@root.route("/")
def home():
    app = flask.current_app
    ip = request.remote_addr
    query = GeobazaQuery()
    resp = query.get(ip)

    data = {
        "hour": datetime.now().strftime("%H:%M"),
        "ip": ip,
        "location": resp.name
    }
    return render_template('layout.html', **data)

@root.route("/<hour>/", methods=['GET', 'POST'])
def telltime(hour='0'):
    app = flask.current_app
    data = {
        "hour": hour
    }
    return render_template('layout.html', **data)

if __name__ == "__main__":
    app.run()
