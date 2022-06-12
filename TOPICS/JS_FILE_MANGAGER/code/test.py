"""
this code was made to use it to manage 'js bootcamp' project files
using command line 'python jsManager <folder_name>'

HOW IT WORKS:
1. count number of directories in the folder
to make it ordered based on the number of the lesson

2. make new directory with given name as a command line argument

3. change the path to new directory made in step 2

4. create three main files index.html, style.css, main.js

4.1 write some text in index.html --> will be in another file attached to this script
the html file will be linking both style.css and main.js

5. save all new files
6. add those files
7. commit files with saved messages


"""
import os
import sys
# import counting_folders
# #
# # project_name = sys.argv[1]
# # project_index = counting_folders.count_folders_with_zfill(os.getcwd())
# #
# # project_name = project_index + '-' + project_name
# #
# # print(project_name)


string = open("template.html", "r").read()
print(string)

