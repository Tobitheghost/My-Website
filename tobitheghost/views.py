from flask import render_template, redirect, Blueprint, request, flash, url_for, session
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFError
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import time
import json
from .email import check_email
import logging
from .logs import req_log
from .movie_data import movieData
from .templates.games.pixel_art.display_data import sptire_data_j, character_names
from .parcel_data import Parcel
from pprint import pprint
import os

homepage = Blueprint("home", __name__, url_prefix="/")


class Contact_Me(FlaskForm):
    name = StringField("Your Name*", validators=[DataRequired()])
    email = EmailField("Your Email*", validators=[DataRequired(), Email()])
    textarea = TextAreaField("Your Message", validators=[DataRequired()])
    submitbtn = SubmitField("Send Message")
    test = StringField("1 + 5", validators=[DataRequired()])


@homepage.before_request
def send_session():
    logging.basicConfig(
        filename="tobitheghost/utils/site.log",
        filemode="a",
        format=json.dumps(
            [
                {"forwarded_for": request.headers.get("X_FORWARDED_FOR")},
                {"real_ip": request.headers.get("X_REAL_IP")},
                {"host": request.headers.get("HOST")},
                {"request": request.url},
                {"user_agent": str(request.user_agent)},
                {"proxy_ip": request.remote_addr},
                {"date-time": "%(asctime)s"},
                {"line": "%(lineno)d"},
                {"function": "%(funcName)s"},
                {"module": "%(module)s"},
                {"messages": "%(message)s"},
            ]
        ),
        level=logging.DEBUG,
    )
    session_log = {
        "x_real_ip": request.headers.get("X_REAL_IP"),
        "request": request.url,
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    if request.headers.get("X_REAL_IP") in session:
        if session["log"]:
            session["log"].append(session_log)
        else:
            session["log"] = [session_log]
    else:
        session["ip"] = request.headers.get("X_REAL_IP")
        session["log"] = (session_log)
    logging.warn(session)


@homepage.route("/", methods=["GET", "POST"])
def home():
    form = Contact_Me()
    response = None
    if request.method == "POST":
        if form.validate_on_submit():
            response = check_email(
                form.name.data, form.textarea.data, form.email.data, form.test.data
            )
            
        else:
            response = "There seems to be an error with your connection", "error"
        flash(response)
        print(response)
        resonse_log = {
            "response": response,
            "name": form.name.data,
            "email_msg": form.textarea.data,
            "email": form.email.data,
        }
        session["name"] = form.name.data
        session["email"] = form.email.data
        logging.warn(resonse_log)
        return render_template("home.html", form=form, response=response)

    logging.warn(response)
    return render_template("home.html", form=form, response=response)


# Errors
@homepage.errorhandler(CSRFError)
def handle_csrf_error(e):
    logging.warn(e)
    return render_template("csrf_error.html", reason=e.description, handler=True), 400


## Portfolio
@homepage.route("/TexasToms")
def texas():
    logging.warn("texas_toms/texas toms.html")
    return render_template("texas_toms/texas toms.html")


# GXO
@homepage.route("/gxo", methods=["GET", "POST"])
def gxo():
    logging.warn("gxo/gxo.html")
    return render_template("gxo/gxo.html")


@homepage.route("/disp/<content>", methods=["GET", "POST"])
def display(content):
    print(content)
    logging.warn(content)
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


@homepage.route("/close", methods=["GET", "POST"])
def close():
    logging.warn("gxo/close.html")
    return render_template("gxo/close.html")


@homepage.route("/outline_visible", methods=["GET", "POST"])
def outline_visible():
    logging.warn("gxo/outline_visible.html")
    return render_template("gxo/outline_visible.html")


@homepage.route("/outline_invisible", methods=["GET", "POST"])
def outline_invisible():
    logging.warn("gxo/outline_invisible.html")
    return render_template("gxo/outline_invisible.html")


# Games
@homepage.route("/games")
def games():
    logging.warn("games/game_page/game_select.html")
    return render_template(template_name_or_list="games/game_page/game_select.html")


# Maps
@homepage.route("/maps")
def maps():
    logging.warn("parcel_search/maps.html")
    return render_template("parcel_search/maps.html")


@homepage.route("/search")
def search_s():
    query = request.args.get("q")
    q_data = Parcel()
    logging.warn(query)
    if query:
        result = q_data.search(query)
    else:
        result = [
            {"id": "error", "multipolygon": "error", "address": "something went wrong"}
        ]

    return render_template("parcel_search/search_results.html", results=result)


@homepage.route("/results/<addressID>")
def results_(addressID):
    query = addressID
    logging.warn(addressID)
    if query:
        q_data = Parcel()
        result = q_data.viewer(query)

        address = result["full_address"]
        owner = result["owner_name"]
        owner2 = result["owner_name2"]
        land_use = result["landusecode"]
        land_desc = result["landusedesc"]
        asLandVal = result["assessed_land_value"]
        asImpVal = result["assessed_improved_value"]
        ExLandVal = result["exempt_land_value"]
        ExImpVal = result["exempt_improved_value"]
        effDate = result["assessment_effective_date"]

    return render_template(
        "parcel_search/parcel_results.html",
        address=address,
        owner=owner,
        owner2=owner2,
        land_use=land_use,
        land_desc=land_desc,
        asLandVal=asLandVal,
        asImpVal=asImpVal,
        ExLandVal=ExLandVal,
        ExImpVal=ExImpVal,
        effDate=effDate,
    )


# Movies
@homepage.route("/movies")
def movies():
    logging.warn("movies/movies.html")
    listoftitles = movieData["title"].values
    listofdates = movieData["release date"].values
    listofdesc = movieData["gen desc"].values
    listofyoutube = movieData["youtube"].values
    listofposter = movieData["poster"].values
    count = len(listoftitles)
    return render_template(
        "movies/movies.html",
        titles=listoftitles,
        dates=listofdates,
        desc=listofdesc,
        youtube=listofyoutube,
        posters=listofposter,
        count=count,
    )


# Pixel Art
@homepage.route("/character_selection")
def pixel():
    logging.warn("games/pixel_art/character_select.html")
    return render_template("games/pixel_art/character_select.html")


@homepage.route("/character_display/<selected_chr>")
def chr_display(selected_chr):
    logging.warn(selected_chr)
    if selected_chr == "Tammy":
        chr = "pages/games/pixel_art/sprite_sheets/tammy_iso/tammy_iso-spritesheet/tammy_iso-spritesheet.png"
        size_class = "One"

        return render_template(
            "games/pixel_art/character_display.html",
            chr=chr,
            sz_cls=size_class,
            selected_chr=selected_chr,
            chr_name=selected_chr,
            chr_date="11/28/2023",
            chr_inspo="https://www.instagram.com/tammy.weese.142/",
        )

    elif selected_chr == "Brisif":
        chr = "pages/games/pixel_art/sprite_sheets/brisif/brisif-idle/Brisif-idle.gif"
        size_class = "Three"
        return render_template(
            "games/pixel_art/character_display.html",
            chr=chr,
            sz_cls=size_class,
            selected_chr=selected_chr,
            chr_name=selected_chr,
            chr_date="11/28/2023",
            chr_inspo="https://www.instagram.com/unicorn_dust101/",
        )

    elif request.args.get("display"):
        character = request.args.get("chr_selected")
        print(character)
        size_class = request.args.get("chr_class")
        print(selected_chr)
        return render_template(
            "games/pixel_art/walking.html",
            direction=selected_chr,
            chr=character,
            sz_cls=size_class,
        )


@homepage.route("/character_editor", methods=["GET", "POST"])
def editor():
    logging.warn("html_utils/json_data.html")
    chr_select = character_names
    if request.method == "POST":
        chr_name = request.form["chr_select"]
        name = sptire_data_j(chr_name)
        pprint(name[chr_name])
        return render_template(
            "html_utils/json_data copy.html",
            chr_select=chr_select,
            chr_dict=name[chr_name],
        )

    return render_template("html_utils/json_data.html", chr_select=chr_select)


# Utilities
@homepage.route("/utils", methods=["GET", "POST"])
def utils():
    logging.warn("utils")
    path = "Z:\\Coding\\New Site\\tobitheghost"
    directory_list = []

    def walk(og_path, itter=0):
        for item in os.listdir(og_path):
            _path = f"{og_path}\\{item}"
            a_path = os.path.join(og_path, item)
            norm_path = os.path.normpath(_path)
            abspath = os.path.abspath(_path)
            space = itter * "\t"
            if os.path.isdir(_path):
                directory_dict = {
                    "path": _path,
                    "basename": os.path.basename(_path),
                    "file": ["folder"],
                    "dir_int": itter,
                }
                directory_list.append(directory_dict)
                count = itter + 1
                walk(_path, count)
            elif os.path.isfile(_path):
                basename = os.path.basename(_path)
                extention = basename.split(".")[-1]
                directory_dict = {
                    "path": _path,
                    "basename": item,
                    "file": ["file", extention],
                    "dir_int": itter,
                }
                directory_list.append(directory_dict)
            else:
                print("IDK what this is...")
        return directory_list

    dirlist = walk(path)

    return render_template("html_utils/utils.html", dir_list=dirlist)


# with homepage.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))
