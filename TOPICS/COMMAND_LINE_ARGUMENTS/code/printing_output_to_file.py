import subprocess

# with open("../text__files/last_command_ran.txt", 'w') as file,\
#      open("errors.txt", "a") as err:
#     # touch isn't working with windows, if shell is False you will get
#     # an error in the terminal
#     p1 = subprocess.run("touch file.css", stdout=file, stderr=err, shell=True)
#     print("done successfully")

p1 = subprocess.run(["git", "add", "*.gitkeep"], capture_output=True)
print(p1)
p2 = subprocess.run(["git", "commit", "-m", "'folder keeper'"], capture_output=True)
if(p2.returncode != 0):
    print("all .gitkeep files were tracked before")
print(p2)
