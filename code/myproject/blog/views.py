from flask import Flask, Blueprint, render_template, url_for
# import db

blog_blueprints = Blueprint('blog', __name__, template_folder='templates/blog')

@blog_blueprints.route('/blog', methods=['GET'])
def blog():
    return render_template('blog.html')
