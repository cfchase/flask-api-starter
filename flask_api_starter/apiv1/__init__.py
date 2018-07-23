from flask import Blueprint

apiv1 = Blueprint('apiv1', __name__)

from flask_api_starter.apiv1 import errors, status

