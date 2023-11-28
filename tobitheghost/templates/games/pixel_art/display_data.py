import json
from pprint import pprint

print_stuff = False


def banner_path(chr_json_data, chr_json_data_file, ready, not_ready, main_dict):
    chr_banner_image = chr_json_data["banner_image"]
    if chr_banner_image == False:
        chr_banner_image_path = "placeholder/placeholder-banner_image/banner_image.png"
        not_ready["banner_image"] = chr_banner_image
    else:
        chr_banner_image_path = chr_json_data_file["Char_Descriptors"][
            "banner_image path"
        ]

    ready["banner_image"] = chr_banner_image_path
    main_dict["banner_image-path"] = chr_banner_image_path


def icon_path(chr_json_data, chr_json_data_file, ready, not_ready, main_dict):
    chr_icon_image = chr_json_data["icon"]
    if chr_icon_image == False:
        chr_icon_image_path = "placeholder/placeholder-icon/icon.png"
        not_ready["icon"] = chr_icon_image
    else:
        chr_icon_image_path = chr_json_data_file["Char_icon"]["path"]
    ready["icon"] = chr_icon_image_path
    main_dict["icon-path"] = chr_icon_image_path


def spritesheet_path(chr_json_data, chr_json_data_file, ready, not_ready, main_dict):
    main_dict["spritesheet-path"] = chr_json_data_file["Char_Spritesheet"]["path"]
    main_dict["number_of_actions"] = chr_json_data_file["Char_Spritesheet"][
        "number_of_actions"
    ]
    main_dict["spritesheet-width"] = chr_json_data_file["Char_Spritesheet"][
        "spritesheet_width"
    ]
    main_dict["spritesheet-height"] = chr_json_data_file["Char_Spritesheet"][
        "spritesheet_height"
    ]
    main_dict["spritesheet_frame-width"] = chr_json_data_file["Char_Spritesheet"][
        "frame_width"
    ]
    main_dict["spritesheet_frame-height"] = chr_json_data_file["Char_Spritesheet"][
        "frame_height"
    ]
    direction = [
        "left",
        "right",
        "back",
        "front",
    ]
    spr_anmtn = chr_json_data_file["Char_Spritesheet"]["Animations"]
    for car in direction:
        main_dict[f"spritesheet-facing_{car}-number"] = spr_anmtn["face_left"]["numb"]
        main_dict[f"spritesheet-facing_{car}-total_frames"] = spr_anmtn["face_left"][
            "total_frames"
        ]
        main_dict[f"spritesheet-facing_{car}-fps"] = spr_anmtn["face_left"]["fps"]
        main_dict[f"spritesheet-facing_{car}-pixel"] = spr_anmtn["face_left"][
            "pixel_size"
        ]
        main_dict[f"spritesheet-facing_{car}-button_key"] = spr_anmtn["face_left"][
            "button_key"
        ]

    main_dict["description-name"] = chr_json_data_file["Char_Descriptors"]["name"]
    main_dict["description-date"] = chr_json_data_file["Char_Descriptors"]["date"]
    main_dict["description_inspiration-name"] = chr_json_data_file["Char_Descriptors"][
        "Insperation"
    ][0]["name"]
    main_dict["description_inspiration-link"] = chr_json_data_file["Char_Descriptors"][
        "Insperation"
    ][0]["link"]


def url_links(chr_json_data, chr_json_data_file, ready, not_ready, main_dict):
    URL_instagram = chr_json_data_file["URLS"]["instagram"]
    URL_tumblr = chr_json_data_file["URLS"]["tumblr"]
    URL_twitter = chr_json_data_file["URLS"]["twitter"]


def data_file_query(chr_data, dir_name, subdir_name, ready, not_ready, main_dict):
    data = chr_data["data"]
    e_dir = chr_data["extra_dir"][0]
    if data == True:
        with open(
            f"tobitheghost/static/pages/games/pixel_art/sprite_sheets/{dir_name}/{subdir_name}-data/{subdir_name}-data.json"
        ) as chr_data_file:
            chr_json_data = json.load(chr_data_file)
            chr_data_file.close()

        banner_path(chr_data, chr_json_data, ready, not_ready, main_dict)

        icon_path(chr_data, chr_json_data, ready, not_ready, main_dict)

        spritesheet_path(chr_data, chr_json_data, ready, not_ready, main_dict)

        url_links(chr_data, chr_json_data, ready, not_ready, main_dict)

        for key in e_dir:
            if type(extra_dir[key]) == dict:
                for s_key in extra_dir[key]:
                    extra_dir_paths(
                        chr_directory_name,
                        chr_subdirectory_name,
                        extra_dir[key],
                        key,
                        s_key,
                    )
        else:
            extra_dir_paths(chr_directory_name, chr_subdirectory_name, extra_dir, key)
    return


def extra_dir_paths(
    dir_name: str,
    subdir_name: str,
    parent_dict: dict,
    parent_dict_key,
    extra_dict_key="",
):
    key = parent_dict_key
    if extra_dict_key == "":
        chr_dir_3 = f""
        k1 = parent_dict_key
    else:
        sub_key = extra_dict_key
        chr_dir_3 = f"/character_name-{key}_{sub_key}"
        k1 = extra_dict_key
    chr_dir_1 = dir_name
    chr_dir_2 = f"/{subdir_name}-{key}"

    chr_directory_path = f"{chr_dir_1}{chr_dir_2}{chr_dir_3}"

    if parent_dict[k1] == False:
        not_ready_extra_dir[k1] = chr_directory_path
        # print(f"\t\tNot Ready Directory: {chr_directory_path}")
    else:
        ready_extra_dir[k1] = chr_directory_path
        # print(f"\t\tReady Directory: {chr_directory_path}")


with open(
    "tobitheghost/static/pages/games/pixel_art/sprite_sheets/sprite_sheets.json"
) as json_data:
    d = json.load(json_data)
    json_data.close()

character_names = [x for x in d]
character_database: []

for entries in character_names:
    not_ready_extra_dir = {}
    ready_extra_dir = {}
    char_dict = {}
    chr_json = d[entries]
    # pprint(chr_json)
    main_dict = char_dict[entries] = {}
    main_dict["ready"] = chr_json["ready"]
    chr_directory_name = chr_json["directory_name"]
    main_dict["directory-name"] = chr_directory_name
    chr_data = chr_json["data"]
    extra_dir = chr_json["extra_dir"][0]
    chr_ready = chr_json["ready"]
    chr_icon = chr_json["icon"]
    chr_need = chr_json["need"]
    chr_banner_image = chr_json["banner_image"]
    if chr_directory_name == "character_templates":
        chr_subdirectory_name = "character_name"
    else:
        chr_subdirectory_name = chr_directory_name

    main_dict["sub_directory-name"] = chr_subdirectory_name

    data_file_query(
        chr_json,
        chr_directory_name,
        chr_subdirectory_name,
        ready_extra_dir,
        not_ready_extra_dir,
        main_dict,
    )

    # print(char_dict[entries])
    print("")
    pprint(main_dict)

    if print_stuff == True:
        print(f"{entries}\n\nDictionary:")
        pprint(d[entries])
        print(f"\nNot Ready:")
        pprint(not_ready_extra_dir)
        print("\nReady:")
        pprint(ready_extra_dir)
        print("\n", "x" * 100, "\n", "x" * 100, "\n")
