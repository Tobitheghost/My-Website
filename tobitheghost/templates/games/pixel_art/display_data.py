import json
from os import path
from pprint import pprint

print_stuff = False
master_dict = {}

with open(
    "tobitheghost/static/pages/games/pixel_art/sprite_sheets/sprite_sheets.json"
) as json_data:
    entry_names = json.load(json_data)
    json_data.close()

character_names = [x for x in entry_names]
character_database: []
# print(character_names)

def sptire_data_j(entries, thespritefile=entry_names):
    chr_name = ""
    directory_name = ""
    data_path = ""
    data_exist = False
    icon_exist = False
    icon_path = ""
    banner_image_bool = False
    extradir_faceleft_bool = False
    extradir_faceleft_path = ""
    extradir_faceright_bool = False
    extradir_faceright_path = ""
    extradir_faceback_bool = False
    extradir_faceback_path = ""
    extradir_facefront_bool = False
    extradir_facefront_path = ""
    extradir_idle_bool = False
    extradir_idle_path = ""
    extradir_walking_bool = False
    extradir_walking_path = ""
    extradir_buttons_descriptions_bool = False
    extradir_buttons_descriptions_path = ""
    extradir_buttons_directional_bool = False
    extradir_buttons_directional_path = ""
    extradir_buttons_aux_bool = False
    extradir_buttons_aux_path = ""
    extradir_spritesheet_bool = False
    extradir_spritesheet_path = ""
    ready_status = False
    need_list = ""
    char_name = ""
    char_icon_title = ""
    char_icon_path = ""
    char_spritesheet_title = ""
    char_spritesheet_path = ""
    char_spritesheet_number_of_actions = ""
    char_spritesheet_spritesheet_width = ""
    char_spritesheet_spritesheet_height = ""
    char_spritesheet_frame_width = ""
    char_spritesheet_frame_height = ""
    char_spritesheet_Animations_faceleft_path = ""
    char_spritesheet_Animations_faceleft_numb = ""
    char_spritesheet_Animations_faceleft_total_frames = ""
    char_spritesheet_Animations_faceleft_fps = ""
    char_spritesheet_Animations_faceleft_pixel_size = ""
    char_spritesheet_Animations_faceleft_button_key = ""
    char_spritesheet_Animations_faceright_path = ""
    char_spritesheet_Animations_faceright_numb = ""
    char_spritesheet_Animations_faceright_total_frames = ""
    char_spritesheet_Animations_faceright_fps = ""
    char_spritesheet_Animations_faceright_pixel_size = ""
    char_spritesheet_Animations_faceright_button_key = ""
    char_spritesheet_Animations_faceback_path = ""
    char_spritesheet_Animations_faceback_numb = ""
    char_spritesheet_Animations_faceback_total_frames = ""
    char_spritesheet_Animations_faceback_fps = ""
    char_spritesheet_Animations_faceback_pixel_size = ""
    char_spritesheet_Animations_faceback_button_key = ""
    char_spritesheet_Animations_facefront_path = ""
    char_spritesheet_Animations_facefront_numb = ""
    char_spritesheet_Animations_facefront_total_frames = ""
    char_spritesheet_Animations_facefront_fps = ""
    char_spritesheet_Animations_facefront_pixel_size = ""
    char_spritesheet_Animations_facefront_button_key = ""
    char_spritesheet_Animations_idle_path = ""
    char_spritesheet_Animations_idle_numb = ""
    char_spritesheet_Animations_idle_total_frames = ""
    char_spritesheet_Animations_idle_fps = ""
    char_spritesheet_Animations_idle_pixel_size = ""
    char_spritesheet_Animations_idle_button_key = ""
    char_spritesheet_Animations_walking_path = ""
    char_spritesheet_Animations_walking_numb = ""
    char_spritesheet_Animations_walking_total_frames = ""
    char_spritesheet_Animations_walking_fps = ""
    char_spritesheet_Animations_walking_pixel_size = ""
    char_spritesheet_Animations_walking_button_key = ""
    char_spritesheet_Animations_buttons_descriptions_alt_b_1_title = ""
    char_spritesheet_Animations_buttons_descriptions_alt_b_1_path = ""
    char_spritesheet_Animations_buttons_descriptions_alt_b_1_type = ""
    char_spritesheet_Animations_buttons_directional_alt_b_1_title = ""
    char_spritesheet_Animations_buttons_directional_alt_b_1_path = ""
    char_spritesheet_Animations_buttons_directional_alt_b_1_type = ""
    char_spritesheet_Animations_buttons_aux_alt_b_1_title = ""
    char_spritesheet_Animations_buttons_aux_alt_b_1_path = ""
    char_spritesheet_Animations_buttons_aux_alt_b_1_type = ""
    char_descriptors_name = ""
    char_descriptors_date = ""
    char_descriptors_Insperation_name = ""
    char_descriptors_Insperation_link = ""
    char_bannerimage_name = "Placeholder Banner Image"
    char_bannerimage_path = "Z:/Coding/New Site/tobitheghost/static/pages/games/pixel_art/sprite_sheets/placeholder/placeholder-banner_image/banner_image.png"
    url_insta = ""
    url_tumblr = ""
    url_twitter = ""
    status_ready = False
    status_need = False

    dict_data = {
        "chr_name": chr_name,
        "directory_name": directory_name,
        "data_path": data_path,
        "data_exist": data_exist,
        "icon_exist": icon_exist,
        "icon_path": icon_path,
        "banner_image_bool": banner_image_bool,
        "extradir_faceleft_bool": extradir_faceleft_bool,
        "extradir_faceleft_path": extradir_faceleft_path,
        "extradir_faceright_bool": extradir_faceright_bool,
        "extradir_faceright_path": extradir_faceright_path,
        "extradir_faceback_bool": extradir_faceback_bool,
        "extradir_faceback_path": extradir_faceback_path,
        "extradir_facefront_bool": extradir_facefront_bool,
        "extradir_facefront_path": extradir_facefront_path,
        "extradir_idle_bool": extradir_idle_bool,
        "extradir_idle_path": extradir_idle_path,
        "extradir_walking_bool": extradir_walking_bool,
        "extradir_walking_path": extradir_walking_path,
        "extradir_buttons_descriptions_bool": extradir_buttons_descriptions_bool,
        "extradir_buttons_descriptions_path": extradir_buttons_descriptions_path,
        "extradir_buttons_directional_bool": extradir_buttons_directional_bool,
        "extradir_buttons_directional_path": extradir_buttons_directional_path,
        "extradir_buttons_aux_bool": extradir_buttons_aux_bool,
        "extradir_buttons_aux_path": extradir_buttons_aux_path,
        "extradir_spritesheet_bool": extradir_spritesheet_bool,
        "extradir_spritesheet_path": extradir_spritesheet_path,
        "ready_status": ready_status,
        "need_list": need_list,
        "char_name": char_name,
        "char_icon_title": char_icon_title,
        "char_icon_path": char_icon_path,
        "char_spritesheet_title": char_spritesheet_title,
        "char_spritesheet_path": char_spritesheet_path,
        "char_spritesheet_number_of_actions": char_spritesheet_number_of_actions,
        "char_spritesheet_spritesheet_width": char_spritesheet_spritesheet_width,
        "char_spritesheet_spritesheet_height": char_spritesheet_spritesheet_height,
        "char_spritesheet_frame_width": char_spritesheet_frame_width,
        "char_spritesheet_frame_height": char_spritesheet_frame_height,
        "char_spritesheet_Animations_faceleft_path": char_spritesheet_Animations_faceleft_path,
        "char_spritesheet_Animations_faceleft_numb": char_spritesheet_Animations_faceleft_numb,
        "char_spritesheet_Animations_faceleft_total_frames": char_spritesheet_Animations_faceleft_total_frames,
        "char_spritesheet_Animations_faceleft_fps": char_spritesheet_Animations_faceleft_fps,
        "char_spritesheet_Animations_faceleft_pixel_size": char_spritesheet_Animations_faceleft_pixel_size,
        "char_spritesheet_Animations_faceleft_button_key": char_spritesheet_Animations_faceleft_button_key,
        "char_spritesheet_Animations_faceright_path": char_spritesheet_Animations_faceright_path,
        "char_spritesheet_Animations_faceright_numb": char_spritesheet_Animations_faceright_numb,
        "char_spritesheet_Animations_faceright_total_frames": char_spritesheet_Animations_faceright_total_frames,
        "char_spritesheet_Animations_faceright_fps": char_spritesheet_Animations_faceright_fps,
        "char_spritesheet_Animations_faceright_pixel_size": char_spritesheet_Animations_faceright_pixel_size,
        "char_spritesheet_Animations_faceright_button_key": char_spritesheet_Animations_faceright_button_key,
        "char_spritesheet_Animations_faceback_path": char_spritesheet_Animations_faceback_path,
        "char_spritesheet_Animations_faceback_numb": char_spritesheet_Animations_faceback_numb,
        "char_spritesheet_Animations_faceback_total_frames": char_spritesheet_Animations_faceback_total_frames,
        "char_spritesheet_Animations_faceback_fps": char_spritesheet_Animations_faceback_fps,
        "char_spritesheet_Animations_faceback_pixel_size": char_spritesheet_Animations_faceback_pixel_size,
        "char_spritesheet_Animations_faceback_button_key": char_spritesheet_Animations_faceback_button_key,
        "char_spritesheet_Animations_facefront_path": char_spritesheet_Animations_facefront_path,
        "char_spritesheet_Animations_facefront_numb": char_spritesheet_Animations_facefront_numb,
        "char_spritesheet_Animations_facefront_total_frames": char_spritesheet_Animations_facefront_total_frames,
        "char_spritesheet_Animations_facefront_fps": char_spritesheet_Animations_facefront_fps,
        "char_spritesheet_Animations_facefront_pixel_size": char_spritesheet_Animations_facefront_pixel_size,
        "char_spritesheet_Animations_facefront_button_key": char_spritesheet_Animations_facefront_button_key,
        "char_spritesheet_Animations_idle_path": char_spritesheet_Animations_idle_path,
        "char_spritesheet_Animations_idle_numb": char_spritesheet_Animations_idle_numb,
        "char_spritesheet_Animations_idle_total_frames": char_spritesheet_Animations_idle_total_frames,
        "char_spritesheet_Animations_idle_fps": char_spritesheet_Animations_idle_fps,
        "char_spritesheet_Animations_idle_pixel_size": char_spritesheet_Animations_idle_pixel_size,
        "char_spritesheet_Animations_idle_button_key": char_spritesheet_Animations_idle_button_key,
        "char_spritesheet_Animations_walking_path": char_spritesheet_Animations_walking_path,
        "char_spritesheet_Animations_walking_numb": char_spritesheet_Animations_walking_numb,
        "char_spritesheet_Animations_walking_total_frames": char_spritesheet_Animations_walking_total_frames,
        "char_spritesheet_Animations_walking_fps": char_spritesheet_Animations_walking_fps,
        "char_spritesheet_Animations_walking_pixel_size": char_spritesheet_Animations_walking_pixel_size,
        "char_spritesheet_Animations_walking_button_key": char_spritesheet_Animations_walking_button_key,
        "char_spritesheet_Animations_buttons_descriptions_alt_b_1_title": char_spritesheet_Animations_buttons_descriptions_alt_b_1_title,
        "char_spritesheet_Animations_buttons_descriptions_alt_b_1_path": char_spritesheet_Animations_buttons_descriptions_alt_b_1_path,
        "char_spritesheet_Animations_buttons_descriptions_alt_b_1_type": char_spritesheet_Animations_buttons_descriptions_alt_b_1_type,
        "char_spritesheet_Animations_buttons_directional_alt_b_1_title": char_spritesheet_Animations_buttons_directional_alt_b_1_title,
        "char_spritesheet_Animations_buttons_directional_alt_b_1_path": char_spritesheet_Animations_buttons_directional_alt_b_1_path,
        "char_spritesheet_Animations_buttons_directional_alt_b_1_type": char_spritesheet_Animations_buttons_directional_alt_b_1_type,
        "char_spritesheet_Animations_buttons_aux_alt_b_1_title": char_spritesheet_Animations_buttons_aux_alt_b_1_title,
        "char_spritesheet_Animations_buttons_aux_alt_b_1_path": char_spritesheet_Animations_buttons_aux_alt_b_1_path,
        "char_spritesheet_Animations_buttons_aux_alt_b_1_type": char_spritesheet_Animations_buttons_aux_alt_b_1_type,
        "char_descriptors_name": char_descriptors_name,
        "char_descriptors_date": char_descriptors_date,
        "char_descriptors_Insperation_name": char_descriptors_Insperation_name,
        "char_descriptors_Insperation_link": char_descriptors_Insperation_link,
        "char_bannerimage_name": char_bannerimage_name,
        "char_bannerimage_path": char_bannerimage_path,
        "url_insta": url_insta,
        "url_tumblr": url_tumblr,
        "url_twitter": url_twitter,
        "status_ready": status_ready,
        "status_need": status_need,
    }

    def check_data(var, var_str, dict_entry):
        try:
            var = dict_entry
        except KeyError:
            pass
        dict_data[var_str] = var

    check_data(chr_name, "chr_name", thespritefile[entries])
    check_data(
        directory_name, "directory_name", thespritefile[entries]["directory_name"]
    )
    check_data(data_path, "data_path", thespritefile[entries]["data"]["path"])
    check_data(data_exist, "data_exist", thespritefile[entries]["data"]["exist"])
    check_data(icon_exist, "icon_exist", thespritefile[entries]["icon"]["exist"])
    check_data(icon_path, "icon_path", thespritefile[entries]["icon"]["path"])
    check_data(
        banner_image_bool, "banner_image_bool", thespritefile[entries]["banner_image"]
    )
    check_data(
        extradir_faceleft_bool,
        "extradir_faceleft_bool",
        thespritefile[entries]["extra_dir"]["face_left"]["exist"],
    )
    check_data(
        extradir_faceleft_path,
        "extradir_faceleft_path",
        thespritefile[entries]["extra_dir"]["face_left"]["path"],
    )
    check_data(
        extradir_faceright_bool,
        "extradir_faceright_bool",
        thespritefile[entries]["extra_dir"]["face_right"]["exist"],
    )
    check_data(
        extradir_faceright_path,
        "extradir_faceright_path",
        thespritefile[entries]["extra_dir"]["face_right"]["path"],
    )
    check_data(
        extradir_faceback_bool,
        "extradir_faceback_bool",
        thespritefile[entries]["extra_dir"]["face_back"]["exist"],
    )
    check_data(
        extradir_faceback_path,
        "extradir_faceback_path",
        thespritefile[entries]["extra_dir"]["face_back"]["path"],
    )
    check_data(
        extradir_facefront_bool,
        "extradir_facefront_bool",
        thespritefile[entries]["extra_dir"]["face_front"]["exist"],
    )
    check_data(
        extradir_facefront_path,
        "extradir_facefront_path",
        thespritefile[entries]["extra_dir"]["face_front"]["path"],
    )
    check_data(
        extradir_idle_bool,
        "extradir_idle_bool",
        thespritefile[entries]["extra_dir"]["idle"]["exist"],
    )
    check_data(
        extradir_idle_path,
        "extradir_idle_path",
        thespritefile[entries]["extra_dir"]["idle"]["path"],
    )
    check_data(
        extradir_walking_bool,
        "extradir_walking_bool",
        thespritefile[entries]["extra_dir"]["walking"]["exist"],
    )
    check_data(
        extradir_walking_path,
        "extradir_walking_path",
        thespritefile[entries]["extra_dir"]["walking"]["path"],
    )
    check_data(
        extradir_buttons_descriptions_bool,
        "extradir_buttons_descriptions_bool",
        thespritefile[entries]["extra_dir"]["buttons"]["descriptions"]["exist"],
    )
    check_data(
        extradir_buttons_descriptions_path,
        "extradir_buttons_descriptions_path",
        thespritefile[entries]["extra_dir"]["buttons"]["descriptions"]["path"],
    )
    check_data(
        extradir_buttons_directional_bool,
        "extradir_buttons_directional_bool",
        thespritefile[entries]["extra_dir"]["buttons"]["directional"]["exist"],
    )
    check_data(
        extradir_buttons_directional_path,
        "extradir_buttons_directional_path",
        thespritefile[entries]["extra_dir"]["buttons"]["directional"]["path"],
    )
    check_data(
        extradir_buttons_aux_bool,
        "extradir_buttons_aux_bool",
        thespritefile[entries]["extra_dir"]["buttons"]["aux"]["exist"],
    )
    check_data(
        extradir_buttons_aux_path,
        "extradir_buttons_aux_path",
        thespritefile[entries]["extra_dir"]["buttons"]["aux"]["path"],
    )
    check_data(
        extradir_spritesheet_bool,
        "extradir_spritesheet_bool",
        thespritefile[entries]["extra_dir"]["spritesheet"]["exist"],
    )
    check_data(
        extradir_spritesheet_path,
        "extradir_spritesheet_path",
        thespritefile[entries]["extra_dir"]["spritesheet"]["path"],
    )
    check_data(ready_status, "ready_status", thespritefile[entries]["ready"])
    check_data(need_list, "need_list", thespritefile[entries]["need"][0])

    if data_exist:
        with open(data_path) as chr_data_file:
            thedatafile = json.load(chr_data_file)
        chr_data_file.close()

        check_data(char_name, "char_name", thedatafile["Char_name"])
        check_data(char_icon_title, "char_icon_title", thedatafile["Char_icon"]["title"])
        check_data(char_icon_path, "char_icon_path", thedatafile["Char_icon"]["path"])
        check_data(
            char_spritesheet_title,
            "char_spritesheet_title",
            thedatafile["Char_Spritesheet"]["title"],
        )
        check_data(
            char_spritesheet_path,
            "char_spritesheet_path",
            thedatafile["Char_Spritesheet"]["path"],
        )
        check_data(
            char_spritesheet_number_of_actions,
            "char_spritesheet_number_of_actions",
            thedatafile["Char_Spritesheet"]["number_of_actions"],
        )
        check_data(
            char_spritesheet_spritesheet_width,
            "char_spritesheet_spritesheet_width",
            thedatafile["Char_Spritesheet"]["spritesheet_width"],
        )
        check_data(
            char_spritesheet_spritesheet_height,
            "char_spritesheet_spritesheet_height",
            thedatafile["Char_Spritesheet"]["spritesheet_height"],
        )
        check_data(
            char_spritesheet_frame_width,
            "char_spritesheet_frame_width",
            thedatafile["Char_Spritesheet"]["frame_width"],
        )
        check_data(
            char_spritesheet_frame_height,
            "char_spritesheet_frame_height",
            thedatafile["Char_Spritesheet"]["frame_height"],
        )
        check_data(
            char_spritesheet_Animations_faceleft_path,
            "char_spritesheet_Animations_faceleft_path",
            thedatafile["Char_Spritesheet"]["Animations"]["face_left"]["path"],
        )
        check_data(
            char_spritesheet_Animations_faceleft_numb,
            "char_spritesheet_Animations_faceleft_numb",
            thedatafile["Char_Spritesheet"]["Animations"]["face_left"]["numb"],
        )
        check_data(
            char_spritesheet_Animations_faceleft_total_frames,
            "char_spritesheet_Animations_faceleft_total_frames",
            thedatafile["Char_Spritesheet"]["Animations"]["face_left"]["total_frames"],
        )
        check_data(
            char_spritesheet_Animations_faceleft_fps,
            "char_spritesheet_Animations_faceleft_fps",
            thedatafile["Char_Spritesheet"]["Animations"]["face_left"]["fps"],
        )
        check_data(
            char_spritesheet_Animations_faceleft_pixel_size,
            "char_spritesheet_Animations_faceleft_pixel_size",
            thedatafile["Char_Spritesheet"]["Animations"]["face_left"]["pixel_size"],
        )
        check_data(
            char_spritesheet_Animations_faceleft_button_key,
            "char_spritesheet_Animations_faceleft_button_key",
            thedatafile["Char_Spritesheet"]["Animations"]["face_left"]["button_key"],
        )
        check_data(
            char_spritesheet_Animations_faceright_path,
            "char_spritesheet_Animations_faceright_path",
            thedatafile["Char_Spritesheet"]["Animations"]["face_right"]["path"],
        )
        check_data(
            char_spritesheet_Animations_faceright_numb,
            "char_spritesheet_Animations_faceright_numb",
            thedatafile["Char_Spritesheet"]["Animations"]["face_right"]["numb"],
        )
        check_data(
            char_spritesheet_Animations_faceright_total_frames,
            "char_spritesheet_Animations_faceright_total_frames",
            thedatafile["Char_Spritesheet"]["Animations"]["face_right"]["total_frames"],
        )
        check_data(
            char_spritesheet_Animations_faceright_fps,
            "char_spritesheet_Animations_faceright_fps",
            thedatafile["Char_Spritesheet"]["Animations"]["face_right"]["fps"],
        )
        check_data(
            char_spritesheet_Animations_faceright_pixel_size,
            "char_spritesheet_Animations_faceright_pixel_size",
            thedatafile["Char_Spritesheet"]["Animations"]["face_right"]["pixel_size"],
        )
        check_data(
            char_spritesheet_Animations_faceright_button_key,
            "char_spritesheet_Animations_faceright_button_key",
            thedatafile["Char_Spritesheet"]["Animations"]["face_right"]["button_key"],
        )
        check_data(
            char_spritesheet_Animations_faceback_path,
            "char_spritesheet_Animations_faceback_path",
            thedatafile["Char_Spritesheet"]["Animations"]["face_back"]["path"],
        )
        check_data(
            char_spritesheet_Animations_faceback_numb,
            "char_spritesheet_Animations_faceback_numb",
            thedatafile["Char_Spritesheet"]["Animations"]["face_back"]["numb"],
        )
        check_data(
            char_spritesheet_Animations_faceback_total_frames,
            "char_spritesheet_Animations_faceback_total_frames",
            thedatafile["Char_Spritesheet"]["Animations"]["face_back"]["total_frames"],
        )
        check_data(
            char_spritesheet_Animations_faceback_fps,
            "char_spritesheet_Animations_faceback_fps",
            thedatafile["Char_Spritesheet"]["Animations"]["face_back"]["fps"],
        )
        check_data(
            char_spritesheet_Animations_faceback_pixel_size,
            "char_spritesheet_Animations_faceback_pixel_size",
            thedatafile["Char_Spritesheet"]["Animations"]["face_back"]["pixel_size"],
        )
        check_data(
            char_spritesheet_Animations_faceback_button_key,
            "char_spritesheet_Animations_faceback_button_key",
            thedatafile["Char_Spritesheet"]["Animations"]["face_back"]["button_key"],
        )
        check_data(
            char_spritesheet_Animations_facefront_path,
            "char_spritesheet_Animations_facefront_path",
            thedatafile["Char_Spritesheet"]["Animations"]["face_front"]["path"],
        )
        check_data(
            char_spritesheet_Animations_facefront_numb,
            "char_spritesheet_Animations_facefront_numb",
            thedatafile["Char_Spritesheet"]["Animations"]["face_front"]["numb"],
        )
        check_data(
            char_spritesheet_Animations_facefront_total_frames,
            "char_spritesheet_Animations_facefront_total_frames",
            thedatafile["Char_Spritesheet"]["Animations"]["face_front"]["total_frames"],
        )
        check_data(
            char_spritesheet_Animations_facefront_fps,
            "char_spritesheet_Animations_facefront_fps",
            thedatafile["Char_Spritesheet"]["Animations"]["face_front"]["fps"],
        )
        check_data(
            char_spritesheet_Animations_facefront_pixel_size,
            "char_spritesheet_Animations_facefront_pixel_size",
            thedatafile["Char_Spritesheet"]["Animations"]["face_front"]["pixel_size"],
        )
        check_data(
            char_spritesheet_Animations_facefront_button_key,
            "char_spritesheet_Animations_facefront_button_key",
            thedatafile["Char_Spritesheet"]["Animations"]["face_front"]["button_key"],
        )
        check_data(
            char_spritesheet_Animations_idle_path,
            "char_spritesheet_Animations_idle_path",
            thedatafile["Char_Spritesheet"]["Animations"]["idle"]["path"],
        )
        check_data(
            char_spritesheet_Animations_idle_numb,
            "char_spritesheet_Animations_idle_numb",
            thedatafile["Char_Spritesheet"]["Animations"]["idle"]["numb"],
        )
        check_data(
            char_spritesheet_Animations_idle_total_frames,
            "char_spritesheet_Animations_idle_total_frames",
            thedatafile["Char_Spritesheet"]["Animations"]["idle"]["total_frames"],
        )
        check_data(
            char_spritesheet_Animations_idle_fps,
            "char_spritesheet_Animations_idle_fps",
            thedatafile["Char_Spritesheet"]["Animations"]["idle"]["fps"],
        )
        check_data(
            char_spritesheet_Animations_idle_pixel_size,
            "char_spritesheet_Animations_idle_pixel_size",
            thedatafile["Char_Spritesheet"]["Animations"]["idle"]["pixel_size"],
        )
        check_data(
            char_spritesheet_Animations_idle_button_key,
            "char_spritesheet_Animations_idle_button_key",
            thedatafile["Char_Spritesheet"]["Animations"]["idle"]["button_key"],
        )
        check_data(
            char_spritesheet_Animations_walking_path,
            "char_spritesheet_Animations_walking_path",
            thedatafile["Char_Spritesheet"]["Animations"]["walking"]["path"],
        )
        check_data(
            char_spritesheet_Animations_walking_numb,
            "char_spritesheet_Animations_walking_numb",
            thedatafile["Char_Spritesheet"]["Animations"]["walking"]["numb"],
        )
        check_data(
            char_spritesheet_Animations_walking_total_frames,
            "char_spritesheet_Animations_walking_total_frames",
            thedatafile["Char_Spritesheet"]["Animations"]["walking"]["total_frames"],
        )
        check_data(
            char_spritesheet_Animations_walking_fps,
            "char_spritesheet_Animations_walking_fps",
            thedatafile["Char_Spritesheet"]["Animations"]["walking"]["fps"],
        )
        check_data(
            char_spritesheet_Animations_walking_pixel_size,
            "char_spritesheet_Animations_walking_pixel_size",
            thedatafile["Char_Spritesheet"]["Animations"]["walking"]["pixel_size"],
        )
        check_data(
            char_spritesheet_Animations_walking_button_key,
            "char_spritesheet_Animations_walking_button_key",
            thedatafile["Char_Spritesheet"]["Animations"]["walking"]["button_key"],
        )
        check_data(
            char_spritesheet_Animations_buttons_descriptions_alt_b_1_title,
            "char_spritesheet_Animations_buttons_descriptions_alt_b_1_title",
            thedatafile["Char_Spritesheet"]["Animations"]["Buttons"]["descriptions"][
                "alt_button_01"
            ]["title"],
        )
        check_data(
            char_spritesheet_Animations_buttons_descriptions_alt_b_1_path,
            "char_spritesheet_Animations_buttons_descriptions_alt_b_1_path",
            thedatafile["Char_Spritesheet"]["Animations"]["Buttons"]["descriptions"][
                "alt_button_01"
            ]["path"],
        )
        check_data(
            char_spritesheet_Animations_buttons_descriptions_alt_b_1_type,
            "char_spritesheet_Animations_buttons_descriptions_alt_b_1_type",
            thedatafile["Char_Spritesheet"]["Animations"]["Buttons"]["descriptions"][
                "alt_button_01"
            ]["type"],
        )
        check_data(
            char_spritesheet_Animations_buttons_directional_alt_b_1_title,
            "char_spritesheet_Animations_buttons_directional_alt_b_1_title",
            thedatafile["Char_Spritesheet"]["Animations"]["Buttons"]["directional"][
                "alt_button_01"
            ]["title"],
        )
        check_data(
            char_spritesheet_Animations_buttons_directional_alt_b_1_path,
            "char_spritesheet_Animations_buttons_directional_alt_b_1_path",
            thedatafile["Char_Spritesheet"]["Animations"]["Buttons"]["directional"][
                "alt_button_01"
            ]["path"],
        )
        check_data(
            char_spritesheet_Animations_buttons_directional_alt_b_1_type,
            "char_spritesheet_Animations_buttons_directional_alt_b_1_type",
            thedatafile["Char_Spritesheet"]["Animations"]["Buttons"]["directional"][
                "alt_button_01"
            ]["type"],
        )
        check_data(
            char_spritesheet_Animations_buttons_aux_alt_b_1_title,
            "char_spritesheet_Animations_buttons_aux_alt_b_1_title",
            thedatafile["Char_Spritesheet"]["Animations"]["Buttons"]["aux"][
                "alt_button_01"
            ]["title"],
        )
        check_data(
            char_spritesheet_Animations_buttons_aux_alt_b_1_path,
            "char_spritesheet_Animations_buttons_aux_alt_b_1_path",
            thedatafile["Char_Spritesheet"]["Animations"]["Buttons"]["aux"][
                "alt_button_01"
            ]["path"],
        )
        check_data(
            char_spritesheet_Animations_buttons_aux_alt_b_1_type,
            "char_spritesheet_Animations_buttons_aux_alt_b_1_type",
            thedatafile["Char_Spritesheet"]["Animations"]["Buttons"]["aux"][
                "alt_button_01"
            ]["type"],
        )
        check_data(
            char_descriptors_name,
            "char_descriptors_name",
            thedatafile["Char_Descriptors"]["name"],
        )
        check_data(
            char_descriptors_date,
            "char_descriptors_date",
            thedatafile["Char_Descriptors"]["date"],
        )
        check_data(
            char_descriptors_Insperation_name,
            "char_descriptors_Insperation_name",
            thedatafile["Char_Descriptors"]["Insperation"][0]["name"],
        )
        check_data(
            char_descriptors_Insperation_link,
            "char_descriptors_Insperation_link",
            thedatafile["Char_Descriptors"]["Insperation"][0]["link"],
        )
        check_data(
            char_bannerimage_name,
            "char_bannerimage_name",
            thedatafile["Char_Descriptors"]["banner_image"]["name"],
        )
        check_data(
            char_bannerimage_path,
            "char_bannerimage_path",
            thedatafile["Char_Descriptors"]["banner_image"]["path"],
        )
        check_data(url_insta, "url_insta", thedatafile["URLS"]["instagram"])
        check_data(url_tumblr, "url_tumblr", thedatafile["URLS"]["tumblr"])
        check_data(url_twitter, "url_twitter", thedatafile["URLS"]["twitter"])
        check_data(status_ready, "status_ready", thedatafile["Status"]["Ready"])
        check_data(status_need, "status_need", thedatafile["Status"]["Need"])

    the_master_dict = {entries: dict_data}
    return the_master_dict

# for item in character_names:
#     print(sptire_data_j(item))
