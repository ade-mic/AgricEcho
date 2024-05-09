from flask import Blueprint
from flask_restful import Api
from post_resource import PostResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(PostResource, '/api/posts', '/api/posts/<string:post_id>')
