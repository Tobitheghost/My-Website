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
from .parcel_search_data import data, land_use_code
from .movie_data import movieData


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


@app.route("/games")
def games():
    return render_template(template_name_or_list="games/game_page/game_select.html")


@app.route("/maps")
def maps():
    return render_template("parcel_search/maps.html")


@app.route("/search")
def search():
    q = request.args.get("q")
    if q:
        res = data[data["ADDRESS"].str.lower().astype(str).str.startswith(str(q))][
            ["ADDRESS"]
        ].head(50)
        ind = data[data["ADDRESS"].str.lower().astype(str).str.startswith(str(q))][
            ["OBJECTID"]
        ].head(50)
        loc = data[data["ADDRESS"].str.lower().astype(str).str.startswith(str(q))][
            ["the_geom"]
        ].head(50)

        loc = loc.values
        res = res.values
        ind = ind.values

        result_content = []
        loc_content = []
        index_content = []
        for x in range(len(res)):
            parcelpolygon = []
            multipolygon = loc[x]
            multipolygon = multipolygon[0]
            multipolygon = multipolygon.split("(((")[1]
            multipolygon = multipolygon.split(")))")[0]
            multipolygon = multipolygon.split(",")
            for item in multipolygon:
                item = item.replace(" -", "-")
                y = [item.split(" ")[1], item.split(" ")[0]]
                parcelpolygon.append(y)
            combo_result = res[x]
            combo_loc = parcelpolygon
            combo_index = ind[x]
            result_content.append(combo_result)
            loc_content.append(combo_loc)
            index_content.append(combo_index)
        res = result_content
        loc = loc_content
        ind = index_content
    else:
        res = [[]]
        loc = [[]]
        ind = [[]]
    return render_template(
        "parcel_search/search_results.html", results=res, location=loc, addr_index=ind
    )


@app.route("/results/<addressID>")
def results(addressID):
    q = addressID
    if q:

        def stringify(index):
            val = data[data["OBJECTID"].astype(str).str.contains(str(q))][[index]]
            value = val.values[0][0]
            if str(value) == "nan":
                value = ""
            else:
                value = str(value)
            return value

        def moneyfy(index):
            valueAmt = stringify(index)
            if "." in valueAmt:
                valueAmt = valueAmt.split(".")[0]
                if len(valueAmt) / 3 > 1.0:
                    count = len(valueAmt) // 3
                    for iter in range(count):
                        if (iter + 1) * 3 == len(valueAmt) - iter:
                            pass
                        else:
                            comaNumb = -1 * ((3 * (iter + 1)) + iter)
                            valueAmt = (
                                valueAmt[:(comaNumb)] + "," + valueAmt[(comaNumb):]
                            )
                valueAmt = f"${valueAmt}.00"
            elif valueAmt == "0":
                valueAmt = f"${valueAmt}.00"
            else:
                valueAmt = "0"
                valueAmt = f"${valueAmt}.00"
            return valueAmt

        address = stringify("ADDRESS")
        owner = stringify("OWN_NAME")
        owner2 = stringify("OWN_NAME2")

        luc = stringify("LANDUSECODE")
        luc = str(luc)
        if "." in luc:
            luc = luc.split(".")[0]
            land_use = land_use_code[luc]
        elif luc == "":
            land_use = ""
        else:
            land_use = luc

        asLandVal = moneyfy("ASSESSED_LAND_VALUE")
        asImpVal = moneyfy("ASSESSED_IMPROVE_VALUE")
        ExLandVal = moneyfy("EXEMPT_LAND_VALUE")
        ExImpVal = moneyfy("EXEMPT_IMPROVE_VALUE")
        effDate = stringify("ASSESSMENT_EFFECTIVE_DATE")

        if effDate == "":
            effDate = "Unlisted"
        if len(effDate) > 3:
            effDate = effDate.split(" ")[0]

    return render_template(
        "parcel_search/parcel_results.html",
        parcel=q,
        address=address,
        owner=owner,
        owner2=owner2,
        land_use=land_use,
        asLandVal=asLandVal,
        asImpVal=asImpVal,
        ExLandVal=ExLandVal,
        ExImpVal=ExImpVal,
        effDate=effDate,
    )


@app.route("/movies")
def movies():
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


@app.route("/character_selection")
def pixel():
    return render_template("games/pixel_art/character_select.html")


@app.route("/character_display/<selected_chr>")
def chr_display(selected_chr):
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
