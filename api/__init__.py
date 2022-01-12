import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from flask_cors import CORS
from api.config import config

db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "dev")
    CORS(app)
    app.config.from_object(config[env]) 
    print(app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)  # initialize Flask SQLALchemy with this flask app
    Migrate(app, db)
    
    # db = SQLAlchemy(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    # migrate = Migrate(app, db)


    from api.inventory.routes import inventory_service

    # Register blueprint(s)
    app.register_blueprint(inventory_service)
    
    

    return app