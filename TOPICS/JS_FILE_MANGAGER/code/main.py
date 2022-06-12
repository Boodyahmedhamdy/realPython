import counting_folders
import os
import sys
import subprocess
import colored_text

# hold project name passed as a command line arguments
project_name = sys.argv[1]

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

# adding files
# -----------------
# ---------------------------------------
# html file
adding_html = subprocess.run(["git", "add", f"{html_file.name}"], capture_output=True)

if adding_html.returncode != 0:
    print(colored_text.make_red(f"something went wrong while adding {html_file.name}"))

commiting_html = subprocess.run(["git", "commit", "-m", 'index file'], capture_output=True)
if commiting_html.returncode != 0:
    print(colored_text.make_red(f"something went wrong while commiting {html_file.name}"))

else:
    print(colored_text.make_green(f"{html_file.name} has been commited successfully"))

# ------------------------------------
# css file
adding_css = subprocess.run(["git", "add", f"{css_file.name}"], capture_output=True)

if adding_css.returncode != 0:
    print(colored_text.make_red(f"something went wrong while adding {css_file.name}"))

commiting_css = subprocess.run(["git", "commit", "-m", 'style file'], capture_output=True)
if commiting_html.returncode != 0:
    print(colored_text.make_red(f"something went wrong while commiting {css_file.name}"))
else:
    print(colored_text.make_green(f"{css_file.name} has been commited successfully"))

# -------------------------------------
# js file
adding_js = subprocess.run(["git", "add", f"{js_file.name}"], capture_output=True)

if adding_js.returncode != 0:
    print(colored_text.make_red(f"something went wrong while adding {js_file.name}"))

commiting_js = subprocess.run(["git", "commit", "-m", 'main js file'], capture_output=True)
if commiting_js.returncode != 0:
    print(colored_text.make_red(f"something went wrong while commiting {js_file.name}"))
else:
    print(colored_text.make_green(f"{js_file.name} has been commited successfully"))

# ------------------------------------
# show success message
print("all files has been added and commited now they are ready to be pushed")

# opening directory in vscode
print("opening vscode to this directory...")

opening_vscode = subprocess.run("code .", capture_output=True, shell=True)
if opening_vscode.returncode != 0:
    print(colored_text.make_red("something went wrong while opening vscode"))
else:
    print(colored_text.make_green("enjoy your development"))
