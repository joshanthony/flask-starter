from flask import request, jsonify, abort

from app.models import Post
from . import posts_blueprint

@posts_blueprint.route('/', methods=['POST', 'GET'])
def all_posts():
    if request.method == "POST":
        name = str(request.data.get('name', ''))
        if name:
            post = Post(name=name)
            post.save()
            response = jsonify({
                'id': post.id,
                'name': post.name,
                'date_created': post.date_created,
                'date_modified': post.date_modified
            })
            response.status_code = 201
            return response
    else:
        # GET request
        posts = Post.get_all()
        results = []

        for post in posts:
            obj = {
                'id': post.id,
                'name': post.name,
                'date_created': post.date_created,
                'date_modified': post.date_modified
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

@posts_blueprint.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_post(id, **kwargs):
    post = Post.query.filter_by(id=id).first()
    if not post:
        abort(404)

    if request.method == 'DELETE':
        post.delete()
        return {
        "message": "post {} was deleted successfully".format(post.id) 
        }, 200

    elif request.method == 'PUT':
        name = str(request.data.get('name', ''))
        post.name = name
        post.save()
        response = jsonify({
            'id': post.id,
            'name': post.name,
            'date_created': post.date_created,
            'date_modified': post.date_modified
        })
        response.status_code = 200
        return response
    else:
        # GET request
        response = jsonify({
            'id': post.id,
            'name': post.name,
            'date_created': post.date_created,
            'date_modified': post.date_modified
        })
        response.status_code = 200
        return response