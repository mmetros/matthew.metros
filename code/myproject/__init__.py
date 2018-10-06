from flask import Flask
import sqlite3

app = Flask(__name__)

# define db before blueprints use them


from myproject.about.views import about_blueprints
from myproject.blog.views import blog_blueprints
from myproject.projects.views import projects_blueprints
from myproject.resume.views import resume_blueprints


# grab our application and call our blueprints
app.register_blueprint(about_blueprints,url_prefix='/about')
app.register_blueprint(blog_blueprints,url_prefix='/blog')
app.register_blueprint(projects_blueprints,url_prefix='/projects')
app.register_blueprint(resume_blueprints,url_prefix='/resume')
