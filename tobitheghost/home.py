from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
    Request,
)
from flask_mail import Mail, Message
from .utils.utils import mail_username
from . import mail, app
import logging
from .logs import req_log


@app.route("/", methods=["GET", "POST"])
def home():
    req_log()
    if request.method == "POST":
        name = request.form.get("name_field")
        email = request.form.get("email_field")
        contact_msg = request.form.get("email_body")
        msg = Message(
            subject=f"ContactWebpage: {name} at {email}",
            body=contact_msg,
            recipients=[mail_username],
            sender=email,
        )
        mail.send(msg)
        msg2 = Message(
            subject=f"Thank You for Contacting Me!",
            body="Thank you for getting in contact with me. I will read your message asap!",
            recipients=[email],
            sender=mail_username,
        )
        mail.send(msg2)
        return render_template("home.html", success=True)
    return render_template("home.html")


@app.route("/TexasToms")
def texas():
    return render_template("texas_toms/texas toms.html")


@app.route("/gxo", methods=["GET", "POST"])
def gxo():
    return render_template("gxo/gxo.html")


@app.route("/disp/<content>", methods=["GET", "POST"])
def display(content):
    print(content)
    image = "pages/gxo/map_media/maxresdefault.jpg"
    video = "pages/gxo/map_media/istockphoto-463918882-640_adpp_is.mp4"
    if content == "Russ":
        return render_template("gxo/display.html", image=image)
    if content == "Bathroom":
        return render_template("gxo/display.html", image=image)
    if content == "Loading_1":
        return render_template(
            "gxo/display.html", image="pages/gxo/map_media/truck-loading-goods.1.1.jpg"
        )
    if content == "Loading_2":
        return render_template(
            "gxo/display.html", image="pages/gxo/map_media/19710556_m.jpg"
        )
    if content == "Loading_3":
        return render_template(
            "gxo/display_video.html",
            video="pages/gxo/map_media/istockphoto-1366683418-640_adpp_is.mp4",
        )
    if content == "New_Pick":
        return render_template(
            "gxo/display.html", image="pages/gxo/map_media/maxresdefault.jpg"
        )
    if content == "Damage":
        return render_template("gxo/display.html", image=image)
    if content == "Charging":
        return render_template(
            "gxo/display_video.html",
            video="pages/gxo/map_media/istockphoto-1400033393-640_adpp_is.mp4",
        )
    if content == "Office":
        return render_template(
            "gxo/display_video.html",
            video="pages/gxo/map_media/istockphoto-1201224615-640_adpp_is.mp4",
        )
    if content == "Break":
        return render_template(
            "gxo/display_video.html",
            video="pages/gxo/map_media/istockphoto-463918882-640_adpp_is.mp4",
        )
    if content == "Forklift":
        return render_template("gxo/display.html", image=image)
    if content == "Wrapping":
        return render_template(
            "gxo/display_video.html",
            video="pages/gxo/map_media/istockphoto-1166568867-640_adpp_is.mp4",
        )
    if content == "Amazon":
        return render_template(
            "gxo/display_video.html",
            video="pages/gxo/map_media/istockphoto-1334942634-640_adpp_is.mp4",
        )
    if content == "Unloading":
        return render_template(
            "gxo/display.html", image="pages/gxo/map_media/Manc-Airport-PR-image-3.jpg"
        )
    return render_template("gxo/display.html", image=image)


@app.route("/close", methods=["GET", "POST"])
def close():
    return render_template("gxo/close.html")


@app.route("/outline_visible", methods=["GET", "POST"])
def outline_visible():
    return render_template("gxo/outline_visible.html")


@app.route("/outline_invisible", methods=["GET", "POST"])
def outline_invisible():
    return render_template("gxo/outline_invisible.html")
