def decorator_1(function):
    def wrapper():
        print("before function running .. ")

        function()

        print("after function end ..")
    return wrapper


@decorator_1
def function():
    print([x for x in range(1, 3)])


function()
