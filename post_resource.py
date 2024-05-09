    #!/usr/bin/python3
"""RESTful API for managing posts using Flask-Restful."""
from flask import Flask, request, g
from flask_restful import Api, Resource, fields, marshal_with
from flask_login import login_required
from models import storage
from models.post import Post

app = Flask(__name__)
api = Api(app)

# Fields for serialization
post_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'user_id': fields.String
}

class PostResource(Resource):
    """Class to handle CRUD operations for posts."""

    @marshal_with(post_fields)
    def get(self, post_id=None):
        """Get a specific post by post_id"""
        if post_id is None:
            posts = storage.all(Post)
            result = [{'id': post.id, 'title': post.title} for post in posts]
            return result
        # specific post
        post = storage.get(Post, id=post_id)
        if post:
            return post
        else:
            return {'message': 'Post not found'}, 404

    @login_required
    @marshal_with(post_fields)
    def post(self):
        """Create a new post"""
        data = request.get_json()
        new_post = Post(title=data.get('title'), content=data.get('content'), user_id=g.user.id)
        storage.new(new_post)
        storage.save()
        return new_post, 201

    @login_required
    @marshal_with(post_fields)
    def put(self, post_id):
        """Update an existing post by post_id"""
        post = storage.get(Post, id=post_id)
        if not post:
            return {'message': 'Post not found'}, 404
        data = request.get_json()
        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        storage.save()
        return post

    @login_required
    def delete(self, post_id):
        """Delete a post by post_id"""
        post = storage.get(Post, id=post_id)
        if not post:
            return {'message': 'Post not found'}, 404
        storage.delete(post)
        storage.save()
        return {'message': 'Post deleted successfully'}


