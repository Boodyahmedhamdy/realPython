from colorama import Fore


def mk_green(thing):
    return f"{Fore.GREEN + thing + Fore.RESET}"


def mk_red(thing):
    return f"{Fore.RED + thing + Fore.RESET}"


def mk_blue(thing):
    return f"{Fore.BLUE + thing + Fore.RESET}"


def mk_yellow(thing):
    return f"{Fore.YELLOW + thing + Fore.RESET}"
