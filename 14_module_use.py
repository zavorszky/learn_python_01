# Project: 01
# File:    14_module_use.py
# Author:  zavorszky@yahoo.com


print("** 1 **")
import module_14a_def

module_14a_def.greeting("Dani")

print("\n** 2 **")
name2 = module_14a_def.person1["name"]
age2 = module_14a_def.person1["age"]
module_14a_def.greeting(name2)
print(f"{age2} éves vagy.")

print("\n** 3 **")
import module_14b_def as m14b

name3 = m14b.person1["name"]
age3 = m14b.person1["age"]
module_14a_def.greeting(name3)
print(f"{age3} éves vagy.")

print("\n** 4 **")
import platform

platformSys = platform.system()
print(platformSys)

print("\n** 5a **")
dirPlatform = dir(platform)
for item5a in dirPlatform:
    print(item5a)

print("\n** 5b **")
dirModule14a = dir(module_14a_def)
for item5b in dirModule14a:
    print(item5b)

print("\n** 6 **")
from module_14c_def import vip

print(vip["name"])
