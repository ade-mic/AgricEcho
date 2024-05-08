#!/usr/bin/python3
"""RESTful API for managing posts using Flask-Restful. """
from flask import Flask, request, g
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_login import login_required
from models import storage
from models.post import Post
api = Api()

# Fields for serialization
post_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String
}

class PostResource(Resource):
    """class that inherits from Resource to handle CRUD operations for posts."""

    @marshal_with(post_fields)
    def get(self, post_id):
        """Logic to get a specific post by post_id"""
        post = storage.get(Post, id=post_id)
        return {'post_id': post.id, 'title': post.title, 'content': post.content}

    @login_required
    def post(self):
        """Post an article API"""
        if g.user is None:
            return {'message': 'Unathorised'}, 401

        data = request.get_json()
        # Logic to create a new post using data, associated with logged-in user
        new_post  = Post(title=data['title'], content=data['content'],
                         user_id=g.user.id)
        storage.new(new_post)
        storage.save()
        return {'message': 'Post created successfully'}, 201

    @login_required
    def put(self):
        """Update an Article API"""
        if g.user is None:
            return {'message': 'Unathorised'}, 401
        data = request.get_json()
        # Logic to update an existing post by post_id using data
        storage.update(data)
        storage.save()
        return {'message': 'Post updated successfully'}

    def delete(self, post_id):
        # Logic to delete a post by post_id
        return {'message': 'Post deleted successfully'}

# Register API resources with Flask app
api.add_resource(PostResource, '/posts', '/posts/<int:post_id>')
