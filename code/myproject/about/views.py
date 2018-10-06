from flask import Flask, Blueprint, render_template, url_for
# import db

about_blueprints = Blueprint('about', __name__, template_folder='templates/about')

@about_blueprints.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
