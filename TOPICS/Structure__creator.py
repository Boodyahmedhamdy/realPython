from colorama import Fore, init
import subprocess
import os

init(autoreset=True)


def make_green(thing):
    return f'{Fore.GREEN + str(thing) + Fore.RESET}'


def createStructure():

    # take name of the folder
    nameOfParent = input("what is the name of TOPIC : ").upper().strip()

    # names of folders
    listOfFolders = ["code", 'resources', 'text__files', "project", "databases"]

    for folder in listOfFolders:
        # create folders first
        os.makedirs(f'{nameOfParent}/{folder}')

        # create .gitkeep file to save the structure for the repo
        with open(f'{nameOfParent}/{folder}/.gitkeep', 'a') as gitkeepFile:

            # handling add to staging area first
            gitkeepAddProcess = subprocess.run(["git", "add", f'{gitkeepFile.name}'],
                                               capture_output=True)
            # if something went wrong
            if gitkeepAddProcess.returncode != 0:
                print(f"something went wrong while adding {gitkeepFile.name}")

            # handling commit with saved message
            gitkeepCommitProcess = subprocess.run(["git", "commit", "-m", "folder keeper"],
                                                  capture_output=True)

            # if something went wrong
            if gitkeepCommitProcess.returncode != 0:
                print(f"something went wrong while commiting {gitkeepFile.name}")

        # create readme file
        with open(f'{nameOfParent}/{folder}/README.md', 'a') as readmeFile:
            readmeFile.write(f"# {folder} folder")
            readmeFile.close()

            readmeAddProcess = subprocess.run(["git", "add", f'{readmeFile.name}'],
                                              capture_output=True)
            if readmeAddProcess.returncode != 0:
                print(f"something went wrong while adding {readmeFile.name}")

            readmeCommitProcess = subprocess.run(["git", "commit", "-m", "README File"],
                                                 capture_output=True)

            if readmeCommitProcess.returncode != 0:
                print(f"something went wrong while commit {readmeFile.name}")

    print(make_green("structure was made successfully ❤ and ready to be pushed"))


createStructure()


# import shutil
# shutil.rmtree("SHIT".upper())
