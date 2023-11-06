from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for,Request
from flask_mail import Mail, Message
from .utils.utils import mail_username
from . import mail
import logging
from .logs import req_log


homePage = Blueprint('home',__name__)

@homePage.route('/', methods=['GET', 'POST'])
def home():
    req_log()
    if request.method == "POST":
        name = request.form.get('name_field')
        email = request.form.get('email_field')
        contact_msg = request.form.get('email_body')
        msg = Message(subject=f"ContactWebpage: {name} at {email}", body=contact_msg, recipients=[mail_username], sender=email)
        mail.send(msg)
        msg2 = Message(subject=f"Thank You for Contacting Me!", body="Thank you for getting in contact with me. I will read your message asap!", recipients=[email], sender=mail_username)
        mail.send(msg2)
        return render_template("home.html", success=True)
    return render_template('home.html')