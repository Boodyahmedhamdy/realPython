from colorama import Fore, init

init(autoreset=True)


def make_green(thing):
    return f'{Fore.GREEN + str(thing) + Fore.RESET}'

def createStructure():

    # take name of the folder
    nameOfParent = input("what is the name of TOPIC : ").upper().strip()

    import os
    os.makedirs(f"{nameOfParent}/code")
    os.makedirs(f"{nameOfParent}/resources")
    os.makedirs(f"{nameOfParent}/text__files")
    os.makedirs(f"{nameOfParent}/PROJECTS")

    print(make_green("structure was made successfully ❤"))

createStructure()


# import shutil
# shutil.rmtree("SHIT".upper())
