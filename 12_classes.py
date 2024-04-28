# Project: 01
# File:    12_classes.py
# Author:  zavorszky@yahoo.com

print("** 1 **")


class Cars:
    color = "piros"


mycar = Cars()
print(f"A kocsim szine: {mycar.color}")

print("\n** 2 **")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


istvan = Person("István", 65)

print(f"Az 1. személy neve: {istvan.name}, kora: {istvan.age}")

# Egy objektum nyomtatható jellemzőjének beállítása.
# Ez másszóval a karakterlánc ábrázolása.
print("\n** 3 **")


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


peter = Person2("Péter", 61)
print(f"A 2. személy neve: {peter.name}, kora: {peter.age}")
