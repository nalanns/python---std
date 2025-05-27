# with open("file.txt", "r") as f:
#     #ALL OF MY CODE
#     content = f.read()

# file = open("file.txt", "r")
# content = file.read()
# file.close()
# print(content)


# file = open("file.txt", "w")
# file.write("Hello, World!\n")
# file.close()
# # Now reading the file to verify the content
# file = open("file.txt", "r")
# content = file.read()
# file.close()
# print(content)

# with open("file.txt", "w") as file:
#     file.write("Hello, World!\n")
# # Now reading the file to verify the content
# with open("file.txt", "r") as file:
#     content = file.read()
# print(content) 

# with open("file.txt", "a") as file:
#     file.write("ekleme \n")
# # Now reading the file to verify the content
# with open("file.txt", "r") as file:
#     content = file.read()
# print(content) 



###################################
from os import *
#mkdir("new_folder") # This will create a new folder named "new_folder" in the current directory
#chdir("new_folder") # Change the current working directory to "new_folder"
#rmdir("new_folder") # This will remove the "new_folder" directory
#rename("new_folder", "newer_folder") # This will rename "file.txt" to "new_file.txt"
rmdir("newer_folder") # This will remove the "newer_folder" directory 

