from colorama import Fore, init

init(autoreset=True)


def make_green(thing):
    return f'{Fore.GREEN + str(thing) + Fore.RESET}'


def createStructure():

    # take name of the folder
    nameOfParent = input("what is the name of TOPIC : ").upper().strip()

    import os
    listOfFolders = ["code", 'resources', 'text__files', "project"]

    for folder in listOfFolders:
        os.makedirs(f'{nameOfParent}/{folder}')
        open(f'{nameOfParent}/{folder}/.gitkeep', 'a')

    print(make_green("structure was made successfully ❤"))


createStructure()


# import shutil
# shutil.rmtree("SHIT".upper())
