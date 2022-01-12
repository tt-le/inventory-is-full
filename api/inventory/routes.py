from api import inventory
from api.inventory.postgres_dao import postres_dao
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify, \
                  make_response, url_for


inventory_service = Blueprint('inventory', __name__, url_prefix='/inventory')

def json_parser(json):
    pass

@inventory_service.route('/product', methods=['POST'])
def create_product():
    try:
        postres_dao().create_product(123,"junior chiecken", 2.99, 2)
    except Exception as e:
        return make_response(e,500)
    return make_response("done",201)

@inventory_service.route('/product', methods=['GET'])
def get_product():
    try:
        postres_dao().get_product()
        pass
    except Exception as e:
        pass
    return

@inventory_service.route('/product', methods=['PUT', 'PATCH'])
def update_product():
    try:
        pass
    except Exception as e:
        pass
    return

@inventory_service.route('/product', methods=['POST', 'DELETE'])
def delete_product():
    try:
        pass
    except Exception as e:
        pass
    return
