from flask import Flask
from flask_cors import CORS
import os
import jinja2

current_dir = os.path.dirname(os.path.abspath(__file__))
app_templates = os.path.join(current_dir, 'templates')
shared_templates = os.path.join(os.path.dirname(os.path.dirname(current_dir)), 'templates')

app = Flask(__name__)
app.jinja_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader([app_templates, shared_templates])
])
CORS(app)
from . import routes