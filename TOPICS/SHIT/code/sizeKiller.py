import time
from tqdm import tqdm
from colorama import Fore


def kill_memory():
    with open("../text__files/file.txt", 'w') as f:
        n = 0
        start = time.time()
        for n in tqdm(range(1, 999), desc=f"writing in file.txt"):
            if n % 2 == 0:
                f.write(Fore.GREEN + f'{n} is an even number\n' + Fore.RESET)
            elif n % 7 == 0:
                f.write(Fore.RED + f'{n} is an normal number\n' + Fore.RESET)
            else:
                f.write(f'{n} is a number\n')

        takenTime = time.time() - start

    print('done in', takenTime, 'seconds')

kill_memory()

