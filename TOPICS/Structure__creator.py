from colorama import Fore, init

init(autoreset=True)


def make_green(thing):
    return f'{Fore.GREEN + str(thing) + Fore.RESET}'


def createStructure():

    # take name of the folder
    nameOfParent = input("what is the name of TOPIC : ").upper().strip()

    import os

    # names of folders
    listOfFolders = ["code", 'resources', 'text__files', "project", "databases"]

    for folder in listOfFolders:
        # create folders first
        os.makedirs(f'{nameOfParent}/{folder}')

        # create .gitkeep file to save the structure for the repo
        open(f'{nameOfParent}/{folder}/.gitkeep', 'a')

        # create readme file
        with open(f'{nameOfParent}/{folder}/README.md', 'a') as readmeFile:
            readmeFile.write(f"# {folder} folder")

    print(make_green("structure was made successfully ❤"))


createStructure()


# import shutil
# shutil.rmtree("SHIT".upper())
