def decorator(func):
    def wrapper(*args):
        for i in args:
            if i < 0:
                print('you have at least one negative number')
                break

        func(*args)

    return wrapper


def d2(func2):
    def wrapper(*args):
        print('it has started')

        func2(*args)

    return wrapper

@d2
@decorator
def printNums(*numbers):
    for i in numbers:
        print(i)


printNums(1, 2, 4, 5, -1, 9, 0)
