from flask import Flask
import os

app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
app.config['SECRET_KEY'] = 'you-will-never-guess'

from my_app import routes