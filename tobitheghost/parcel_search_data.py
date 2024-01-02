import pandas as pd
from pprint import pprint
from math import isnan

data = pd.read_csv("tobitheghost/static/pages/parcel/Parcels_data.csv")
content = data.iloc[1]

print_log = False

def check_nan(entry):
    if type(entry) is not str:
        if isnan(entry):
            entry = ""
    return entry

def check_usd(numb):
    new_numb = numb
    if str(numb) == "0.0":
        new_numb = ""
    else:
        try:
            new_numb = str(int(numb))
            i = -3
            continueing = True
            while continueing == True:
                if len(new_numb) > i*-1:
                    new_numb = f'{new_numb[:i]},{new_numb[i:]}'
                    i -= 4
                else: 
                    continueing = False
        except ValueError:
            pass
        new_numb = f'${new_numb}.00'
    return new_numb

def check_land_use(numb):
    # print(f"Land Use: {numb} Type: {type(numb)} Raw {repr(numb)}")
    if numb == "":
        pass
        new_numb = numb
        use = "Unknown Use"
    else:
        new_numb = str(int(numb))
        if new_numb in land_use_code.keys():
            use = land_use_code[new_numb]
        else:
            use = "Unknown Use"
    return new_numb, use

def check_int(numb):
        try:
            numb = int(numb)
        except ValueError:
            pass

titles = ['the_geom', 'OBJECTID', 'PARCELTYPE', 'KIVAPIN', 'APN', 'PLATNAME',
        'LOT', 'BLOCK', 'TRACT', 'OWN_NAME', 'OWN_NAME2', 'OWN_ADDR',
        'OWN_ADDR2', 'OWN_CITY', 'OWN_STATE', 'OWN_ZIP', 'ADDRESS', 'ADDR',
        'FRACTION', 'PREFIX', 'STREET', 'STREET_TYPE', 'SUITE', 'LANDUSECODE',
        'ASSESSED_LAND_VALUE', 'ASSESSED_IMPROVE_VALUE', 'EXEMPT_LAND_VALUE',
        'EXEMPT_IMPROVE_VALUE', 'ASSESSMENT_EFFECTIVE_DATE', 'LEGAL',
        'SHAPE.AREA', 'SHAPE.LEN']

land_use_code = {
    "1111": "Single Family (Non-Mobile Home Park)",
    "1112": "Mobile Home Park",
    "1121": "Townhouse",
    "1122": "Duplex",
    "1123": "Multifamily - 3 units",
    "1124": "Multifamily - 4 units",
    "1125": "Multifamily - 5 units or greater",
    "1126": "Condominium",
    "1200": "Hotel / Motel",
    "2100": "Commercial (Non-Office)",
    "2300": "Office",
    "3110": "Heavy Industry",
    "3120": "Light Industry / Storage / Distribution / Vehicle Sale / Service",
    "3200": "Solid Waste Management",
    "4110": "School",
    "4120": "Training Outside Classrooms",
    "4130": "Library",
    "4200": "Emergency Response / Public Safety",
    "4300": "Utilities",
    "4500": "Medical",
    "4600": "Cemetery",
    "4700": "Military Base",
    "4800": "Institutional",
    "5100": "Pedestrian Movement",
    "5211": "Garage",
    "5212": "Paved Parking / Other Paved Lots",
    "5220": "Driving",
    "5400": "Railroad",
    "5500": "Water-Based Movement",
    "5600": "Airport",
    "5700": "Spacecraft",
    "6100": "Bus",
    "6200": "Spectator Sports",
    "6300": "Theater",
    "6400": "Convention and Exhibition",
    "6500": "Mass Training and Drills",
    "6610": "Social or Cultural Assembly",
    "6620": "Church",
    "6700": "Museum",
    "6800": "Historical",
    "7100": "Park",
    "7200": "Golf Course",
    "7310": "Condominium Common Area",
    "7320": "Single Family Common Area",
    "7330": "Duplex / Townhouse Common Area",
    "7340": "Multifamily - 3 units - Common Area",
    "7350": "Multifamily - 4 units - Common Area",
    "7360": "Multifamily - 5+ units - Common Area",
    "7400": "Other Recreation",
    "8100": "Agricultural",
    "8200": "Horticultural",
    "8300": "Extraction",
    "8400": "Forest / Logging",
    "9100": "Not Applicable",
    "9210": "Single Family untested for acreage",
    "9220": "Industrial untested for heavy / light",
    "9230": "Outbuilding untested for surroundings",
    "9240": "Misc. improvement untested for surroundings",
    "9250": "Building on Leased Land",
    "9260": "Exempt",
    "9270": "Locally Assessed",
    "9280": "Condo untested for residence or common area",
    "9300": "Underground Space",
    "9400": "Permanent Open Space (e.g. flood)",
    "9500": "Vacant Residential",
    "9600": "Vacant Non-Residential (including billboards)"
}

def pt(p, n, t = titles):
    remainder = int(str(p).split(".")[1])
    p = int(p)
    up = "\x1B[3A" # ANSI control codes
    clr = "\x1B[0K"
    loop_percentage = int((n / 31)*100)
    loop_per_remainder = 100 - loop_percentage
    l_p = "█"*loop_percentage
    l_r = "-"*loop_per_remainder
    l_bar = f"~[{l_p}{l_r}]~"
    re_remainder = 100 - remainder
    r_p = "█"*remainder
    r_r = "-"*re_remainder
    r_bar = f"~[{r_p}{r_r}]~"
    print(f"{up}Loop:      {l_bar}{clr}\nRemainder: {r_bar}{clr}\nProgress  ({p}%){clr}")
    # print(f"{bar} --- {p}%", end='\r')
    if print_log == True:
        print(t[n])
top = data.dtypes

# for x in range(len(data.index)):
#     percent = round((x / len(data.index))*100, 2)
#     # if print_log == False:
#         # print(f"{percent}%", end='\r')
#         # # print(f"{percent}%")

#     item = data.iloc[x]["the_geom"].replace("MULTIPOLYGON (((", "").replace(")))", "").replace(", ", ",").split(",")
    
#     pt(percent,0)
#     new__the_geom = [[x.split(" ")[0], x.split(" ")[1]] for x in item]
#     pt(percent,3)
#     new__KIVAPIN=check_nan(data.iloc[x]["KIVAPIN"])
#     pt(percent,4)
#     new__APN=check_nan(data.iloc[x]["APN"])
#     pt(percent,5)
#     new__PLATNAME=check_nan(data.iloc[x]["PLATNAME"])
#     pt(percent,6)
#     new__LOT=check_nan(data.iloc[x]["LOT"])
#     pt(percent,7)
#     new__BLOCK=check_nan(data.iloc[x]["BLOCK"])
#     pt(percent,8)
#     new__TRACT=check_nan(data.iloc[x]["TRACT"])
#     pt(percent,9)
#     new__OWN_NAME=check_nan(data.iloc[x]["OWN_NAME"])
#     pt(percent,10)
#     new__OWN_NAME2=check_nan(data.iloc[x]["OWN_NAME2"])
#     pt(percent,11)
#     new__OWN_ADDR=check_nan(data.iloc[x]["OWN_ADDR"])
#     pt(percent,12)
#     new__OWN_ADDR2=check_nan(data.iloc[x]["OWN_ADDR2"])
#     pt(percent,13)
#     new__OWN_CITY=check_nan(data.iloc[x]["OWN_CITY"])
#     pt(percent,14)
#     new__OWN_STATE=check_nan(data.iloc[x]["OWN_STATE"])
#     pt(percent,15)
#     new__OWN_ZIP=check_int(check_nan(data.iloc[x]["OWN_ZIP"]))
#     comma_query = ""
#     if new__OWN_ADDR2 != "":
#         comma_query = f" {new__OWN_ADDR2}, "
#     new_OWNER_full_address = f"{new__OWN_ADDR}, {comma_query}{new__OWN_CITY}, {new__OWN_STATE} {new__OWN_ZIP}"
#     pt(percent,16)
#     new__ADDRESS=check_nan(data.iloc[x]["ADDRESS"])
#     pt(percent,17)
#     new__ADDR=check_nan(data.iloc[x]["ADDR"])
    

#     pt(percent,18)
#     new__FRACTION=check_nan(data.iloc[x]["FRACTION"])
#     pt(percent,19)
#     new__PREFIX=check_nan(data.iloc[x]["PREFIX"])
#     pt(percent,20)
#     new__STREET=check_nan(data.iloc[x]["STREET"])
#     pt(percent,21)
#     new__STREET_TYPE=check_nan(data.iloc[x]["STREET_TYPE"])
#     pt(percent,22)
#     new__SUITE=check_nan(data.iloc[x]["SUITE"])
#     new_full_address = f"{new__ADDR} {new__STREET} {new__STREET_TYPE}."
#     owner_occupied = False
#     owner_occupied_str = "False"
#     chx = 0
#     # print(f"new__ADDRESS == new__OWN_ADDR:{new__ADDRESS == new__OWN_ADDR}")
#     # print(f"new__OWN_ADDR.split(' ')[0]:{new__OWN_ADDR.split(' ')[0]}")
#     # print(f"new__ADDRESS in new__OWN_ADDR.split(' ')[0]:{new__ADDR in new__OWN_ADDR.split(' ')[0]}")
#     try:
#         if new__ADDRESS == new__OWN_ADDR:
#             chx = 1
#     except:
#         pass
#     try:
#         if new__ADDR in new__OWN_ADDR.split(" ")[0]:
#             chx = 1
#     except TypeError:
#         pass
#     if chx == 1:
#         new_full_address = new_OWNER_full_address
#         owner_occupied = True
#         owner_occupied_str = "True"
#     pt(percent,23)
#     new__LANDUSECODE, new__LANDUSEDESC=check_land_use(check_nan(data.iloc[x]["LANDUSECODE"]))
#     pt(percent,24)
#     new__ASSESSED_LAND_VALUE=check_usd(check_nan(data.iloc[x]["ASSESSED_LAND_VALUE"]))
#     pt(percent,25)
#     new__ASSESSED_IMPROVE_VALUE=check_usd(check_nan(data.iloc[x]["ASSESSED_IMPROVE_VALUE"]))
#     pt(percent,26)
#     new__EXEMPT_LAND_VALUE=check_usd(check_nan(data.iloc[x]["EXEMPT_LAND_VALUE"]))
#     pt(percent,27)
#     new__EXEMPT_IMPROVE_VALUE=check_usd(check_nan(data.iloc[x]["EXEMPT_IMPROVE_VALUE"]))
#     pt(percent,28)
#     new__ASSESSMENT_EFFECTIVE_DATE=check_nan(data.iloc[x]["ASSESSMENT_EFFECTIVE_DATE"])
#     pt(percent,29)
#     new__LEGAL=check_nan(data.iloc[x]["LEGAL"])
#     pt(percent,30)
#     new__SHAPE_AREA=check_nan(data.iloc[x]["SHAPE.AREA"])
#     pt(percent,31)
#     new__SHAPE_LEN=check_nan(data.iloc[x]["SHAPE.LEN"])

#     if print_log == True:
#         print(f"\033[0;32mKIVAPIN:\033[0m {new__KIVAPIN}")
#         print(f"\033[0;32mAPN:\033[0m {new__APN}")
#         print(f"\033[0;32mPLATNAME:\033[0m {new__PLATNAME}")
#         print(f"\033[0;32mLOT:\033[0m {new__LOT}")
#         print(f"\033[0;32mBLOCK:\033[0m {new__BLOCK}")
#         print(f"\033[0;32mTRACT:\033[0m {new__TRACT}")
#         print(f"\033[0;32mOwner Name:\033[0m {new__OWN_NAME}")
#         print(f"\033[0;32mOwner Name 2:\033[0m {new__OWN_NAME2}")
#         print(f"\033[0;32mOwner Occupied:\033[0m {owner_occupied_str}")
#         print(f"\033[0;32mOwner Address:\033[0m {new__OWN_ADDR}")
#         print(f"\033[0;32mOwner Address 2:\033[0m {new__OWN_ADDR2}")
#         print(f"\033[0;32mOwner City:\033[0m {new__OWN_CITY}")
#         print(f"\033[0;32mOwner State:\033[0m {new__OWN_STATE}")
#         print(f"\033[0;32mOwner Zip:\033[0m {new__OWN_ZIP}")
#         print(f"\033[0;32mOwner Full Address:\033[0m {new_OWNER_full_address}")
#         print(f"\033[0;32mNew Address:\033[0m {new__ADDRESS}")
#         print(f"\033[0;32mNew Street Numbers:\033[0m {new__ADDR}")
#         print(f"\033[0;32mNew Fraction:\033[0m {new__FRACTION}")
#         print(f"\033[0;32mNew Prefix:\033[0m {new__PREFIX}")
#         print(f"\033[0;32mNew Street Name:\033[0m {new__STREET}")
#         print(f"\033[0;32mNew Street Type:\033[0m {new__STREET_TYPE}")
#         print(f"\033[0;32mNew Suite:\033[0m {new__SUITE}")
#         print(f"\033[0;32mNew Full Address:\033[0m {new_full_address}")
#         print(f"\033[0;32mNew Land Use Code:\033[0m {new__LANDUSECODE}")
#         print(f"\033[0;32mNew Land Use Description:\033[0m {new__LANDUSEDESC}")
#         print(f"\033[0;32mNew Land Value:\033[0m {new__ASSESSED_LAND_VALUE}")
#         print(f"\033[0;32mNew Improved Land Value:\033[0m {new__ASSESSED_IMPROVE_VALUE}")
#         print(f"\033[0;32mNew Exempt Land Value:\033[0m {new__EXEMPT_LAND_VALUE}")
#         print(f"\033[0;32mNew Exempt Improve Value:\033[0m {new__EXEMPT_IMPROVE_VALUE}")
#         print(f"\033[0;32mNew Assessment Effective Date:\033[0m {new__ASSESSMENT_EFFECTIVE_DATE}")
#         print(f"\033[0;32mNew Legal:\033[0m {new__LEGAL}")
#         print(f"\033[0;32mNew Shape Area:\033[0m {new__SHAPE_AREA}")
#         print(f"\033[0;32mNew Shape Legnth:\033[0m {new__SHAPE_LEN}")
#         print("\n\n\n")
    
#     # a = input()
#     # if a == "x":
#         # break


# # pprint(item)
