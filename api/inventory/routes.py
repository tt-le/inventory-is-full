from werkzeug.wrappers import response
from api import inventory
from api.inventory.postgres_dao import postgres_dao
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify, \
                  make_response, url_for
from api.inventory.utils import validate_json, validate_schema
from api.inventory.schemas.item_schema import create_item, update_item
from sqlalchemy.exc import NoResultFound

inventory_service = Blueprint('inventory', __name__, url_prefix='/inventory')


def generate_csv():
    pass

@inventory_service.route('/product', methods=['POST'])
@validate_json
@validate_schema(create_item)
def create_product():
    response = {'success': False,
                'message':'',
                'payload':{}}
    try:
        payload = g.parsed_json
        product = postgres_dao().create_product(**payload)
        response['success'] = True
        response['message'] = "CREATE-OK"
        response['payload'] = product
        code = 201
    except BaseException as e:
        # TODO Should log the exception instead and write a relevant message back
        response['message']=repr(e)
        code = 500
    finally:
        return make_response(jsonify(response), code)
    

@inventory_service.route('/product/<id>', methods=['GET'])
def get_product(id):
    response = {'success': False,
                'message':'',
                'payload':{}}
    try:
        product = postgres_dao().get_product(id)
        response['success'] = True
        response['message'] = "OK"
        response['payload'] = product
        code = 200
    except NoResultFound as e:
        response['message'] = f"No product found with id: {id}"
        code = 404
    except BaseException as e:
        # TODO Should log the exception instead and write a relevant message back
        response['message']=repr(e)
        code = 500
    finally:
        return make_response(jsonify(response), code)

@inventory_service.route('/product/<id>', methods=['PUT', 'PATCH'])
@validate_json
@validate_schema(update_item)
def update_product(id):
    response = {'success': False,
                'message':'',
                'payload':{}}
    try:
        payload = g.parsed_json
        product = postgres_dao().update_product(id=id,fields=payload)
        response['success'] = True
        response['message'] = "UPDATE-OK"
        response['payload'] = product
        code = 200
        return make_response(response, 201)
    except NoResultFound as e:
        response['message'] = f"No product found with id: {id}"
        code = 404
    except BaseException as e:
        # TODO Should log the exception instead and write a relevant message back
        response['message']=repr(e)
        code = 500
    finally:
        return make_response(jsonify(response), code)

@inventory_service.route('/product/<id>', methods=['POST', 'DELETE'])
def delete_product(id):
    response = {'success': False,
                'message':'',
                'payload':{}}
    try:
        product = postgres_dao().delete_product(id)
        response['success'] = True
        response['message'] = "DELETE-OK"
        response['payload'] = product
        code = 200
    except NoResultFound as e:
        response['message'] = f"No product found with id: {id}"
        code = 404
    except BaseException as e:
        # TODO Should log the exception instead and write a relevant message back
        response['message']=repr(e)
        code = 500
    finally:
        return make_response(jsonify(response), code)
