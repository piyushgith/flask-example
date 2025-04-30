from flask import render_template
from app import app
from app.forms import LoginForm

# This file contains the route definitions for the Flask application.
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Piyush'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Bangalore!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


# ...

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)