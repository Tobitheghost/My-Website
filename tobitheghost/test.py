import os
from pprint import pprint

# print(os.listdir("Z:\\Coding\\New Site\\tobitheghost"))
path = "Z:\\Coding\\New Site\\tobitheghost"

directory_list = []

def walk(og_path, itter=0):
    for item in os.listdir(og_path):
        _path = f"{og_path}\\{item}"
        a_path = os.path.join(og_path, item)
        norm_path = os.path.normpath(_path)
        abspath = os.path.abspath(_path)
        space = itter*'\t'
        # print(f"{space}{og_path}\\{item}\t{itter}")
        if os.path.isdir(_path):
            directory_dict = {"path": _path, "basename": os.path.basename(_path), "file": ["folder"], "dir_int": itter}
            directory_list.append(directory_dict)
            count = itter + 1
            walk(_path, count)
        elif os.path.isfile(_path):
            basename = os.path.basename(_path)
            extention = basename.split(".")[-1]
            directory_dict = {"path": _path, "basename": item, "file": ["file", extention], "dir_int": itter}
            directory_list.append(directory_dict)
        else:
            print("IDK what this is...")
        
        # print(f"\tPath:          {_path}\n\tJoined Path:   {a_path}\n\tNormal Path:   {norm_path}\n\tAbsolute Path: {abspath}\n")
    return directory_list

dirlist = walk(path)

for item in dirlist:
    pprint(item)
    print()