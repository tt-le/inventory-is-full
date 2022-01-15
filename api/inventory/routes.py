from dataclasses import asdict
from werkzeug.wrappers import response
from api import inventory
from api.inventory.models import Base
from api.inventory.postgres_dao import postgres_dao
from flask import Blueprint, g, jsonify, make_response
from api.inventory.utils import validate_json, validate_schema, export_csv
from api.inventory.schemas.item_schema import create_item, update_item
from sqlalchemy.exc import NoResultFound

inventory_service = Blueprint('inventory', __name__, url_prefix='/inventory')

@inventory_service.route('/product/export', methods=['GET'])
def generate_csv():
    response = make_response()
    try:
        products = postgres_dao().get_all_product()
        product_fields = postgres_dao().get_product_field_names()[2:]
        response.set_data(export_csv(products,product_fields))
        response.headers["Content-Disposition"] = "attachment; filename=Products.csv"
        response.headers["Content-type"] = "text/csv"
        response.status_code = 200
        return response
    except BaseException as e:
        # TODO Should log the exception instead and write a relevant message back
        return make_response({'message':repr(e)}, 500)
    
@inventory_service.route('/product', methods=['POST'])
@validate_json
@validate_schema(create_item)
def create_product():
    response = {'message':'',
                'payload':{}}
    try:
        payload = g.parsed_json
        product = postgres_dao().create_product(**payload)
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
    response = {'message':'',
                'payload':{}}
    try:
        product = postgres_dao().get_product(id)
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
    response = {'message':'',
                'payload':{}}
    try:
        payload = g.parsed_json
        product = postgres_dao().update_product(id=id,fields=payload)
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
    response = {'message':'',
                'payload':{}}
    try:
        product = postgres_dao().delete_product(id)
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
