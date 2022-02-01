import os
from datetime import datetime


print(os.getcwd())  # printing what's in current working directory

# os.chdir(r"C:/Users/User/PycharmProjects/Scripting With Python")  # chdir: change directory

print(os.listdir())
# you can pass a path in list directory
# but by default it will print the list files and folders present in the current directory

# os.mkdir('Folder') : here mkdir means make directory and will create only one directory/folder
# os.makedirs('Folder/inner folder') : will create deep directories, all at a time
# Example:
# os.makedirs("folder/inner folder")  # easy to use

# to delete directories: os.rmdir and os.removedirs
# os.removedirs() is dangerous. USE os.rmdir() TO REMOVE SPECIFIC DIRECTORIES!!
# Example:
# os.rmdir("Folder/inner folder")
# os.removedirs("Folder/inner folder")

# to rename:
# os.rename("File", "Renamed File")
# (name of the original file, what you want to rename the file)

# looking at the information of a file/folder using .stat:
print((os.stat('astro.jpg')))
print((os.stat('astro.jpg')).st_size)  # printing the size
print((os.stat('astro.jpg')).st_mtime)  # printing the modification time (but i don't understand what it's printing?!!)

# printing modification time in human readable format:
# oops! have to import datetime module. Look at the top

mo_time = (os.stat('astro.jpg')).st_mtime
print(datetime.fromtimestamp(mo_time))  # passing mo_time

# walk method tutorial in corey schafers video (10:09)
