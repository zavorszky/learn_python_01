# Project: 01
# File:    21_readFile.py
# Author:  zavorszky@yahoo.com

fileOperationMode_read = "r"
fileOperationMode_append = "a"
fileOperationMode_write = "w"
fileHandlingMode_text = "t"


print("** 1 **")
fname = "21_readFile_demo.txt"
print(f"A {fname} file beolvasása...")
fileOpenMode = fileOperationMode_read + fileHandlingMode_text
f = open(fname, fileOpenMode)
print(f.read())
f.close()

print("\n** 2 **")
n = 5
f = open(fname, fileOpenMode)
print(f"A {fname} file első {n} karakterének beolvasása...")
print(f.read(n))
f.close()

print("\n** 3 **")
f = open(fname, fileOpenMode)
print(f"A {fname} file első 2 sorának beolvasása...")
print(f.readline())
print(f.readline())
f.close()

print("\n** 4 **")
f = open(fname)
i = 0
print(f"A {fname} file beolvasása soronként...")
for line in f:
    i += 1
    print(f"{i}. {line}")
f.close()

print("\n** 5.a **")
fname_original = "21_readFile_original.txt"
fname_new = "21_readFile_new.txt"
# fname_extended = "21_readFile_extended.txt"
print(f"Az eredeti {fname_original} file másolása: {fname_new}")
f_from = open(fname_original, fileOperationMode_read + fileHandlingMode_text)
f_to = open(fname_new, fileOperationMode_write + fileHandlingMode_text)
for line in f_from:
    f_to.writelines(line)
f_to.close()
f_from.close()

print("\n** 5.b **")
extensionLine = "Now the file has more content!"
print(f"Az {fname_new} file kiegészítése a '{extensionLine}' sorral")
f = open(fname_new, fileOperationMode_append + fileHandlingMode_text)
f.write("\n" + extensionLine)
f.close()

f = open(fname_new, fileOperationMode_read + fileHandlingMode_text)
print(f.read())
f.close()

print("\n** 6 **")
import os

if os.path.exists(fname_new):
    print(f"Törlöm a {fname_new} file-t...")
    os.remove(fname_new)
else:
    print(f"A {fname_new} file nem létezik, nem törlöm.")
print("Kész!")
