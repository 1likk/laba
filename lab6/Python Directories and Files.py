import os

# path = input()
path = "./"

print("Directories in", path, ":", end = " ")
with os.scandir(path) as it:
    for entry in it:
        if entry.is_dir():
            print(entry.name, end = " ")
print("\n")

print("Files and directories in", path, ":", end = " ")
with os.scandir(path) as it:
    for entry in it:
        print(entry.name, end = " ")
print("\n")

print("Files in", path, ":", end = " ")
with os.scandir(path) as it:
    for entry in it:
        if entry.is_file():
            print(entry.name, end = " ")

#2
import os

# path = input()
path = "./3.py"
print("Existence:", os.access(path, os.F_OK))
print("Readability:", os.access(path, os.R_OK))
print("Writeability:", os.access(path, os.W_OK))
print("Executeability:", os.access(path, os.X_OK))

#3
import os
path = input()

if os.access(path, os.F_OK):
    print("File name:", os.path.basename(path))
    print("Diretory:", os.path.dirname(path))

#4
import os

f = open(r"C:\pp2\Lab 6\dir-and-files\4.py", "r")

print(len(f.readlines()))

#5
import os

def ABC_files_create():
    letter = ord('A')
    for i in range(26):
        file = open(chr(letter) + '.py', 'w')
        file.close()
        letter += 1

# ABC_files_create()

def ABC_files_delete():
    letter = ord('A')
    for i in range(26):
         os.remove(chr(letter) + '.py')
         letter += 1

# ABC_files_delete()

#7
file1 = open('7.py', 'r')
file2 = open('7_copy.py', 'a')

for row in file1:
    file2.write(row)

#8
import os

path = input()

if os.path.exists(path):
    os.remove(path)
else:
    print("No such file was found!")