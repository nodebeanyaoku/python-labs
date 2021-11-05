# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.



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


print(ext_dict)

data = []

with open(data_path.joinpath("filecountsv2.csv"), "a") as csvfile:
    countwriter = csv.writer(csvfile)
    for ext in ext_dict:
        x = (f"{ext_dict[ext]}") 
        data.append(x)
    countwriter.writerow(data)
