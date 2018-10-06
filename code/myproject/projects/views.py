from flask import Flask, Blueprint, render_template, url_for
# import db

projects_blueprints = Blueprint('projects', __name__, template_folder='templates/projects')

@projects_blueprints.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')
