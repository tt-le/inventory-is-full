from dataclasses import asdict
from functools import wraps
from io import StringIO
from flask import (
    jsonify,
    request,
    make_response,
    g
)
from jsonschema import Draft202012Validator
import csv

def export_csv(table, table_fields):
    with StringIO() as io:
        writer = csv.writer(io, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(table_fields)
        for row in table:
            row = list(asdict(row).values())
            writer.writerow(row)
        return io.getvalue()
    
    

def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json
        except Exception as e:
            msg = "payload must be a valid json"
            response = jsonify({'message':msg, 'payload':{'errors':repr(e)}})
            return make_response(response, 400)
        return f(*args, **kw)
    return wrapper

def validate_schema(schema):
    validator = Draft202012Validator(schema)
    def wrapper(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            json = request.json
            print(request)
            print(json)
            errors = [error.message for error in validator.iter_errors(json)]
            if errors:
                response = jsonify({'message':'invalid json','payload':{'errors':errors}})
                return make_response(response, 400)
            else:
                g.parsed_json = {}
                for property in schema['properties']:
                    if property in json:
                        g.parsed_json[property] = json[property]
                return fn(*args, **kwargs)
        return wrapped
    return wrapper