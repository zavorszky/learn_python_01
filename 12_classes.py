# Project: 01
# File:    12_classes.py
# Author:  zavorszky@yahoo.com

print("** 1 **")


class Car:
    color = "piros"


mycar = Car()
print(f"A kocsim szine: {mycar.color}")

print("\n** 2 **")


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age


istvan = Person2("István", 65)

print(f"Az 1. személy neve: {istvan.name}, kora: {istvan.age}")

# Egy objektum nyomtatható jellemzőjének beállítása.
# Ez másszóval a karakterlánc ábrázolása.
print("\n** 3 **")


class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


peter = Person3("Péter", 61)
print(f"A 2. személy neve: {peter.name}, kora: {peter.age}")


print("\n** 4.a **")


class Person4a:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_full_name(self):
        print(f"{self.last_name} {self.first_name}")


zi = Person4a("István", "Závorszky")
zi.print_full_name()

# A "self" helyett bármilyen változó/paraméret/argument név megadható
# csak konzekvensen kell használni.
# Pl. self => ci
print("\n** 4.b **")


class Person4b:
    def __init__(ci, first_name, last_name):
        ci.first_name = first_name
        ci.last_name = last_name

    def print_full_name(ci):
        print(f"{ci.last_name} {ci.first_name}")


zi = Person4b("István", "Závorszky")
zi.print_full_name()
