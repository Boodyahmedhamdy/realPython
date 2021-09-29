def decor(function):
    def inner():
        print('-----------------')
        function()
        print('-----------------')

    return inner

@decor
def my_function():
    print('hello for everyone here')


my_function()


