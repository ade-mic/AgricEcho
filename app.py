#!/usr/bin/python3
"""Renders Home Page"""
from flask import Flask, render_template, redirect, request, url_for, session, flash
from models.base_model import BaseModel, Base
from models.post import Post
from models.user import User
from flask import jsonify
from os import environ
from werkzeug.security import generate_password_hash, check_password_hash
from models.engine.config import SECRET_KEY
# from models.engine.db_storage import DBStorage
from models import storage
import random
import markdown2

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Define routes
@app.route('/')
def index():
    """Render Home Page"""
    all_posts = storage.all(Post)
    # num_articles = min(len(all_posts), 10)
    # top10 = random.sample(list(all_posts), num_articles)
    print(all_posts)
    return render_template('index.html', hot_topics=all_posts)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    """Render SignUp"""
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the email already exists
        existing_user = storage.get(User, email=email)

        if existing_user:
            error = "User already exists"
            flash(error, 'error')
            return render_template('signup.html', error=error)
        else:
            # Hash the password
            hashed_password = generate_password_hash(password)
            # Create a new user and add to the database
            new_user = User(email=email,
                            first_name=first_name,
                            last_name=last_name,
                            password=hashed_password)
            storage.new(new_user)
            storage.save()
            flash('SignUp successful!', 'success')
            return redirect(url_for('signin'))

    return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """Handles Signin requests"""
    if 'user_id' in session:
        # User already signed in, redirect to user_home
        if request.method == 'POST' and request.headers.get('Content-Type') =='application/json':
            return jsonify({'message': 'User is already signed in'}), 400
        # if not api request
        return redirect(url_for('user_home'))

    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            # Handle API request
            data = request.json
            email = data.get('email')
            password = data.get('password')
            # Check if user exists and password matches
            user = storage.get(User, email=email)
            if user and check_password_hash(user.password, password):
                # store user session
                session['user_id'] = user.id
                return jsonify({'message': 'Signin successful'}), 200
            else:
                return jsonify({'error': 'Invalid email or password.'}), 401
        
        # Get form data
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the user exists and password matches
        user = storage.get(User, email=email)
        if user and check_password_hash(user.password, password):
            # Store user session
            session['user_id'] = user.id
            flash('Signin successful!', 'success')
            # Redirect to user homepage
            return redirect(url_for('user_home'))
        else:
            # Authentication failed, render sign-in page with an error message
            error = "Invalid email or password."
            flash(error, 'error')
            return render_template('signin.html', error=error)

    # Handle GET request (render the signin form)
    return render_template('signin.html')


@app.route('/user_home')
def user_home():
    """Handles user home"""
    # Check if user is logged in
    if 'user_id' in session:
        # Render user homepage
        user_posts = storage.get(User, id=session['user_id']).posts
        return render_template('user_home.html', posts=user_posts)
    else:
        # User not logged in, redirect to sign-in page
        return redirect(url_for('signin'))

@app.route('/post_article', methods=['GET', 'POST'])
def post_article():
    """Route for posting article"""
    if request.method == 'POST':
        if 'user_id' in session:
            author_id = session['user_id']
            title = request.form.get('title')
            content = request.form.get('content')
            new_post = Post(title=title, content=content, user_id=author_id)
            storage.new(new_post)
            storage.save()
            return redirect(url_for('user_home'))
    return render_template('index.html')

@app.route('/view_post/<string:post_id>')
def view_post(post_id):
    """Display the full content of a post"""
    post = storage.get(Post, id=post_id)
    if post:
        html_content = markdown2.markdown(post.content)
        return render_template('view_post.html', post=post,
                               html_content=html_content)
    else:
        flash('Post not found!', 'error')
        return redirect(url_for('user_home'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
