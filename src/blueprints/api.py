from flask import Blueprint
from flask_restful import Api

from src.resources.Notes import Notes

# Define a 'workspace' for the api, with the url prefix /api/
# All added resources, should have /api/ in the url.

api_bp = Blueprint("api", __name__, url_prefix="/api")

api = Api(api_bp, errors=Exception)

api.add_resource(Notes, "/notes")
