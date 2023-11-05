import os
from flask import Flask
from flask_mail import Mail
from .utils.utils import mail_password, mail_username, mail_port

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = mail_port
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

def create_app():
    from . import home
    app.register_blueprint(home.homePage)

    return app