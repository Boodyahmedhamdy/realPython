import datetime as dt
from colorama import Fore, init

init(autoreset=True)


def make_green(thing):
    return f'{Fore.GREEN + str(thing) + Fore.RESET}'

today = dt.date.today()
print('today is', make_green(today))
print("year", make_green(today.year))
print("month", make_green(today.month))
print("day", make_green(today.day))


birthday = dt.date(2002, 6, 3)
difference = today - birthday
print('you lived', make_green(difference.days), 'days')


tdelta = dt.timedelta(days=3)
past = today - tdelta
print(past)

