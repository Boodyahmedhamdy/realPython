import counting_folders
import os
import sys
import subprocess
import colored_text
from tqdm import tqdm


def commit_file(file_name: str, commit_message: str):

    commiting_file = subprocess.run(["git", "commit", "-m", commit_message], capture_output=True)
    if commiting_file.returncode != 0:
        print(colored_text.make_red(f"something went wrong while commiting {file_name}"))

    else:
        print(colored_text.make_green(f"{file_name} has been commited successfully"))


def add_file(file_name: str):

    adding_file = subprocess.run(["git", "add", f"{file_name}"], capture_output=True)
    if adding_file.returncode != 0:
        print(colored_text.make_red(f"something went wrong while adding {file_name}"))
    else:
        print(colored_text.make_green(f"{file_name} has been added successfully"))


def add_and_commit_file(file_name: str, commit_message: str):
    add_file(file_name)
    commit_file(file_name, commit_message)


# hold project name passed as a command line arguments
project_name = input("enter name of project: ")

# number of the project in the current directory
project_index = counting_folders.count_folders_with_zfill(os.getcwd())

# prefix project name with index
project_name = project_index + '-' + project_name

# NOW PROJECT NAME IS READY TO BE USED
# ------------------------------------

# create folder with new name
os.mkdir(project_name)
# show success message
print(colored_text.make_green(f"created {project_name} folder successfully"))

# move to the new directory -- it's empty for now
os.chdir(project_name)

# CREATE THREE MAIN FILES
# ----------------------------

# read template to from template.html
html_template = open("../template.html", "r").read()\
    .replace("project_name", project_name)

# open html file in writing mode
html_file = open("index.html", "w")
html_file.write(html_template)
html_file.close()

# create css file -- no need to do something with it
css_file = open("style.css", "w")
css_file.close()

# create main js file -- no need to do something with it
js_file = open("main.js", "w")
js_file.close()


print(colored_text.make_green(f"created {html_file.name, css_file.name, js_file.name} successfully"))

# ALL FILES ARE READY TO BE ADDED AND commit
all_files_with_commit_message = [
    (html_file.name, "index file"),
    (css_file.name, "style file"),
    (js_file.name, "main js file")
]
try:
    for file_name, message in tqdm(all_files_with_commit_message):
        add_and_commit_file(file_name=file_name, commit_message=message)
except Exception as e:
    print(e)


print("all files has been added and commited now they are ready to be pushed")

# opening directory in vscode
print("opening vscode to this directory...")

opening_vscode = subprocess.run("code .", capture_output=True, shell=True)
if opening_vscode.returncode != 0:
    print(colored_text.make_red("something went wrong while opening vscode"))
else:
    print(colored_text.make_green("enjoy your development"))
