import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from flask_cors import CORS
from api.config import config
from time import sleep


db = SQLAlchemy()

def retry_db_connection(app):
    with app.app_context():
        attempts = 2
        while attempts > 0:
            try:
                db.create_all()
                db.session.commit()
                return
            except BaseException as e:
                print(e)
                sleep(5)
                attempts += 1

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "dev")
    CORS(app)
    app.config.from_object(config[env]) 

    db.init_app(app)  # initialize Flask SQLALchemy with this flask app
    Migrate(app, db)
    
    # db = SQLAlchemy(app)
    # migrate = Migrate(app, db)
    from api.inventory.models import Item
    retry_db_connection(app)


    from api.inventory.routes import inventory_service

    # Register blueprint(s)
    app.register_blueprint(inventory_service)
    
    

    return app