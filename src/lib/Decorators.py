from functools import wraps

import flask_restful
from flask import request

def check_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'Content-Type' not in request.headers or 'application/json' not in request.headers['Content-Type'] or request.headers['Content-Type'] != 'application/json':
            flask_restful.abort(400, msg="Content-type is not 'application/json'")
        if not request.is_json:
            flask_restful.abort(400, msg="No valid JSON")
        return func(*args, **kwargs)
    return wrapper