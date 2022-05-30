import time


def timer(function):
    def wrapper(n):
        start_time = time.time()

        function(n)

        end_time = time.time()

        print(f"function: {function.__name__} took {(end_time - start_time)} seconds")
    return wrapper


@timer
def loop(n: int):
    for number in range(n):
        for x in range(number):
            print(number, x)


loop(4)
