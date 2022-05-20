# import the sys module
import sys

# get argc
number_of_passed_args = len(sys.argv)

# the first argument is the name of the script
name_of_script = sys.argv[0]

# print passed arguments
for n, argument_name in enumerate(sys.argv):
    # all of type string even numbers are strings
    print(n, "-->", argument_name, "type is", type(argument_name))









