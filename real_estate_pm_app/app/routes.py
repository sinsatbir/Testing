from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/dashboard')
def dashboard():
    # For now, just render a simple template or return a string
    # We will create dashboard.html in the next step
    return render_template('dashboard.html', title='Dashboard')

@app.route('/create_project')
def create_project():
    # We will create create_project.html in the next step
    return render_template('create_project.html', title='Create New Project')

@app.route('/view_projects')
def view_projects():
    # We will create view_projects.html in the next step
    return render_template('view_projects.html', title='View Projects')
