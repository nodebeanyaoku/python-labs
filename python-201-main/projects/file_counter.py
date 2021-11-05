# Add the code for the file counter script that you wrote in the course.




import pathlib

# locate path of my Desktop
dir = pathlib.Path("/mnt/c/users/nodebechukwu.anyaoku/desktop")

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



