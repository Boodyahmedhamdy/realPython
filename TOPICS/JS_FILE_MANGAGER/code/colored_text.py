from colorama import init, Fore

# should be found for windows
init()


def make_green(string):
    return Fore.GREEN + string + Fore.RESET


def make_red(string):
    return Fore.RED + string + Fore.RESET


