#!/usr/bin/python3
"""Renders Home Page"""
from flask import Flask, render_template, redirect, request, url_for, session, flash
from models.base_model import BaseModel
from models.category import Category
from models.post import Post
from models.tag import Tag
from models.post_tag import PostTag
from models.user import User
from models.base_model import BaseModel, Base
from os import environ
from werkzeug.security import generate_password_hash, check_password_hash
from models.engine.config import SECRET_KEY
# from models.engine.db_storage import DBStorage
from models import storage

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Define routes
@app.route('/')
def index():
    """Render Home Page"""
    return render_template('index.html')

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
        return redirect(url_for('user_home'))

    if request.method == 'POST':
        # Get form data
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the user exists and password matches
        user = storage.get(User, email=email)
        print(user)
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
        return render_template('user_home.html')
    else:
        # User not logged in, redirect to sign-in page
        return redirect(url_for('signin'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

