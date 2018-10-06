from flask import Flask, Blueprint, render_template, url_for
# import db

resume_blueprints = Blueprint('resume', __name__, template_folder='templates/resume')

@resume_blueprints.route('/resume', methods=['GET'])
def resume():
    return render_template('resume.html')
