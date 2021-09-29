# l = [1,2,34,5,6,6,7,8,9,0]
# import sys
# import os
# print(sys.getsizeof(l), "bytes")
# file = open("../text__files/file__1.txt", 'a')
# file.write('ahmed hassan\n')
# file.close()
# print(sys.getsizeof(file))
# os.remove('../text__files/file__1.txt')

lll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = map(lambda i: i**2, lll)
print(next(x))
print(next(x))
print(next(x))
print(next(x))

for q in x:
    print(q)

print('-----------------')
x = range(1, 11)
y = iter(range(1, 11))

print(next(iter(x)))
print(next(iter(x)))
print(next(iter(x)))
print('----------------------------')
print(next(y))
print(next(y))
print(next(y))


