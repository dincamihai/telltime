#!/usr/bin/env python

import telltime

import flask
import flaskext.script

def create_app(instance_path=None):
    app = flask.Flask(__name__.split('.')[0],
                      instance_path=instance_path,
                      instance_relative_config=True)
    app.config.from_pyfile("settings.py", silent=False)
    telltime.initialize_app(app)
    return app

manager = flaskext.script.Manager(create_app)

if __name__ == '__main__':
    manager.run()
