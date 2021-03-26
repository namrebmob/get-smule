# __init__.py

from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_url_path='/public', static_folder='../public')

if app.config['ENV'] == 'production':
    app.config.from_object('app.config.ProductionConfig')
else:
    app.config.from_object('app.config.DevelopmentConfig')

if app.debug:
    from flask_debugtoolbar import DebugToolbarExtension
    debug_toolbar = DebugToolbarExtension(app)

bootstrap = Bootstrap(app)

from . import routes
