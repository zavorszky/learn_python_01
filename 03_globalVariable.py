# Project: 01
# File:    03_globalVariable.py
# Author:  zavorszky@yahoo.com

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

def myfunc2():
    global x2
    x2 = "fantastic"

myfunc2()
print("Python is " + x2)