import time
from colorama import Fore, init
import os

init(autoreset=True)


def make_green(thing):
    return f'{Fore.GREEN + str(thing) + Fore.RESET}'


def count_down(seconds, message):
    while seconds > 0:
        print(seconds)
        seconds = seconds - 1
        time.sleep(1)
    print(str(message))


# count_down(4, 'happy new year !!')
# print(time.gmtime())
print(make_green('the current time is'), time.localtime())

print(make_green('seconds since 1 jun 1970 till now'), time.time(), make_green('seconds'))

# using strftime to display the current time to be readable
# nowTime = time.localtime()  # no need to use it in this case
stringTimeDays = time.strftime("%d /%m /%Y")  # make year only the capital format
stringTimeHours = time.strftime("%H:%M:%S")  # hours are all capital
print(make_green('today is'), stringTimeDays, make_green('using strftime()'))
print(make_green('hours is'), stringTimeHours, make_green('using strftime()'))


# MAKING A HISTORY FOR RUNNING
# write in the file
with open('../text__files/history__time.txt', "a") as historyFileWrite:
    # add new line
    historyFileWrite.write(stringTimeDays + '\t' + stringTimeHours + '\n')
# separator
print("-------------------------\n"
      "histoty"
      "\n-------------------")
# read file
with open('../text__files/history__time.txt', "r") as historyFileRead:
    linesOfFile = historyFileRead.readlines()
    for line in linesOfFile:
        print(linesOfFile.index(line) + 1,
              "-",
              make_green(line),
              end="")

