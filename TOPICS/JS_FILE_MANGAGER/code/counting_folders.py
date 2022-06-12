import os


def count_folders(path: str) -> int:
    # the value to be returned
    number_of_directories = 0

    # some how it should be used this way
    for _, dirs, _ in os.walk(path):
        number_of_directories = len(dirs)
        break

    # return the needed value
    return number_of_directories


def count_folders_with_zfill(path: str) -> str:
    # the value to be returned
    number_of_directories = 0

    # some how it should be used this way
    for _, dirs, _ in os.walk(path):
        number_of_directories = len(dirs)
        break

    # return the needed value
    return str(number_of_directories).zfill(2)