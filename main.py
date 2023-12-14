import os
from flask import Flask, session
from flask_restful import Resource, Api
from application.config import LocalDevelopmentConfig
from application.database import db
from application.models import *
app = None
api = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.secret_key = 'Secret Key'
    if os.getenv('ENV', "development") == "production":
      raise Exception("Currently no production config is setup.")
    else:
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    print("db initialized")
    db.create_all()
    api = Api(app)
    app.app_context().push()
    print("app created successfully")
    return app, api

app, api = create_app()

# Import all the controllers so they are loaded
from application.controllers import *



if __name__ == '__main__':
  # Run the Flask app
  app.run()