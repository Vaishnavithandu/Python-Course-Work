'''

File Operations:

we have 4 types

1) Read Mode :
2) Write Mode :
3) Append Mode :
4) Binary Mode ( Rarely used) :


'''
# if i want to open any file 

# file = open('xyz.txt','r') # error : file not found

# to Avoid error use try and except:

try:
    file = open('demo.txt','r')
    read = file.read()
    print(read) # -- to read a file
except FileNotFoundError:
    print("File is not present")

#-------------------------------------------------------------#

try:
    file = open('demo.txt','r')
    readlines = file.readline()
    print(readlines) # -- to read lines in file in a signle line
except FileNotFoundError:
    print("File is not present")

#--------------------------------------------------------------#

try:
    file = open('demo.txt','r')
    file.seek(10) # gives the file content from index 10
    read = file.read()
    print(read) # -- to read a file
except FileNotFoundError:
    print("File is not present")

#-------------------------------------------------------------#

try:
    file = open('demo.txt','r')
except FileNotFoundError:
    print("File is not present")
else:
    read = file.read()
    file.seek(0)
    readlines=file.readlines() # going to give you list of lines
    file.seek(0) # it's like cursor
    readline = file.readline() # going to give you the 1st line

    print(f"\nFile Content using read():\n{read}")
    print("\nFile Content using readlines():\n{readlines}")
    print(f"\nFile Content using readline():\n{readline}")

finally:
    print("Rest of the code")

'''
2) Write Mode: 
- It is going to create a file if the file is not exists and it won't throw any error.
- If the file is present it opens the present file.

'''

try: 
    file = open('dsda.txt','w')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('Monday we have exam')
finally:
    print("Rest of the Code")

'''
3) Append Mode:

how many times we exceute it append those many times in the file.

'''
# append and read at the same time

try:
    file = open('dsda.txt','a+')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('Monday we have exam\n')
    file.seek(0)
    print(file.read())
    file.close()

finally:
    print("Rest of the Code")

# Append and wrtie at the same time

try:
    file = open('dsda.txt','w+')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('Monday we have exam\n')
    file.seek(0)
    print(file.read())
    file.close()

finally:
    print("Rest of the Code")

# Read and write at same time:

try:
    file = open('dsda.txt','r+')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('Monday we have exam\n')
    file.seek(0)
    print(file.read())
    file.close()

finally:
    print("Rest of the Code")

'''
r - read
w - write
a - append
r+ - read + write
w+ - write + read
a+ - append + read

'''
# with open as --- we need not to close the file 

with open('dsda.text','r+') as file:
    file.write('\nFile operatiions')
    file.seek(0)
    print(file.read())

'''
OS :

this is how you need to create a directory
'''
import os
print(os.getcwd())
os.mkdir('DSDA') # to create a newfloder from python using mkdir  

import os
print(os.getcwd())
if not os.path.exists('DSDA'): # checks if the file path 'DSDA' is there or not.if it's there it won't create another.
    os.mkdir('DSDA')

import os
if not os.path.exists('DSDA'):
    os.rmdir('DSDA') # rmdir works only when we have empty directory.it doesn't work when the file exist

# Folder inside the folder(sub folder):

import os
if not os.path.exists('DSDA'):
    os.mkdir('DSDA')
os.makedirs('DSDA/1415')

# If we want to remove the DSDA folder:
import os
if not os.path.exists('DSDA'):
    os.mkdir('DSDA')
os.makedirs('DSDA/1415')

os.rmdir("DSDA")  # error: folder is not empty.we need an empty directory to remove a folder
shutil.rmtree('DSDA')  # to remove a directory folder use 'rmtree'

# hoe to join a directory in aide a folder:
import os
if not os.path.exists('DSDA'):
    os.mkdir('DSDA')

filepath = os.path.join('DSDA','demo.txt')
