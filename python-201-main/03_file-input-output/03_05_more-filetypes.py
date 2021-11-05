# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.


import pathlib
from pathlib import Path
import csv

# locate path of my Desktop
dir = pathlib.Path("/mnt/c/users/nodebechukwu.anyaoku/desktop")

# Path handling to run script form anywhere
data_path = Path("/home/anyaoku/codingnomads/python-201-main/03_file-input-output")

ext_lst = []
file_list = []
ext_dict = {}
file_dict = {}

# list out all the files in desktop location
for file in dir.iterdir():
    file_list.append(file.suffix)

# store extension not in this list
[ext_lst.append(ext) for ext in file_list if ext not in ext_lst]

ext_dict = dict.fromkeys(ext_lst, None)

for ext in file_list:

    for key, val in ext_dict.items():
        if ext == key:
            ext_dict[key] = file_list.count(ext)


ext_name = []

with open(data_path.joinpath("filecountsv2.csv"), "r") as csvfile:

    reader = csv.DictReader(csvfile, fieldnames= ["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

    print(counts)