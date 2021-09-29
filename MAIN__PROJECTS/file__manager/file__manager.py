# import modules
import os


# COLORING FUNCTIONS
from colorama import Fore, init
init(autoreset=True)

def make_green(thing):
    return f'{Fore.GREEN + str(thing) + Fore.RESET}'

def make_red(thing):
    return f'{Fore.RED + str(thing) + Fore.RESET}'
# =========================================
# =========================================


def show_options():
    print("1- create file\n"
          "2- create folder\n"
          "3- delete file\n"
          "4- delete folder")
# =========================================

# CREATE THE FILE -- ONLY TEXT FILES
def create_file():
    # where we are
    mainDir = os.getcwd()


    # get file name
    fileName = input("enter file name : ")

    # make sure it is a text file
    if not fileName.endswith(".txt"):
        fileName = fileName + ".txt"

    newPath = input(f"where do you want to create this file\n "
                    f"NOTE: this is the current dir {make_green(mainDir)} : ")

    if newPath.isspace():
        open(fileName, "a")

    else:
        # create the file
        open(newPath + '/' + fileName, "a")

    print(make_green("file created succesfully"))

# CREATE A FOLDER
def create_folder():

    dirName = input("please enter the name of directory"
          f" this is the active dir {make_green(mainDir)} : ")

    # create directory
    os.mkdir(dirName)

    print(make_green("folder created successfully"))

# DELETE A FILE
def delete_file():

    filePath = input("enter file path to delete"
                     f"this is the active folder {make_green(mainDir)} : ")

    sure = input(f"are you sure to delete {make_green(filePath)} : ")
    if sure == "y" or sure == "Y":
        os.remove(filePath)
        print(f"{make_green(filePath)} has been deleted successfully")

    else:
        print("no thing happend")

# DELETE THE WHOLE FOLDER
def delete_folder():
    folderPath = input("enter the folder path \n"
                       f"the active path {make_green(mainDir)} :")

    sure = input(f"are you sure to delete {folderPath} \n"
         f"{make_red('warning : this will delete the whole file and its entities')} : ")

    if sure == "y" or sure == "Y":
        import shutil
        shutil.rmtree(folderPath)
        print(make_green("folder has been destroyed"))
    else:
        print("no thing happend")

# SAY HELLO TO THE USER
print("welcome to file manager\n-----------")

# GET THE CURRENT WORKING DIRECTORY
mainDir = os.getcwd()

# show the options for the user
show_options()

# take the operation
operation = input("choose what you want to do : ")

# TAKE THE ORDERS AND RUN ITS FUCTION
if operation == '1':
    create_file()
elif operation == '2':
    create_folder()
elif operation == '3':
    delete_file()
elif operation == '4':
    delete_folder()
else:
    print(make_red("invalid operation"))
