import os

print(os.getcwd())

os.chdir("../")


print(os.getcwd())

for _, dirs, files in os.walk(os.getcwd()):
    print(dirs, files)
    print(len(dirs), len(files))
    print(len(dirs))
    break

# print(os.walk(os.getcwd()))

# path, dirs, files = os.walk(os.getcwd())
# print(path, len(dirs), files)

