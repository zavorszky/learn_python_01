# Project: 01
# File:    09_for_and_range.py
# Author:  zavorszky@yahoo.com

print('** 1 **')
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print('\n** 2 **')
for letter in "banana":
    print(letter)

# A "range()"-nél figyelni kell, hogy a megadott felsőhatárt
# nem adja: range(6) : [0, 1, ... 5]
print('\n** 3.a **')
for i in range(6):
    print(f"i = {i}")

# A "range()" kezdőértékkel.
# range(2, 6) : [2, 3, ... 5]
print('\n** 3.b **')
for i in range(2, 6):
    print(f"i = {i}")

# A "range()"-nek megadható a növekmény (lépés/step) is.
# range(2, 6, 3) : [2, 5]
# range(2, 8, 3) : [2, 5]
# range(2, 9, 3) : [2, 5, 8]
print('\n** 3.c **')
for i in range(2, 6, 3):
    print(f"i = {i}")

# A "for" esetén is használható az "else:".
print('\n** 4.a **')
for i in range(6):
    print(f"i = {i}")
else:
    print(f"A ciklus végetért {i}")

# Ha a "for"-ból "break"-el lépünk ki, akkor az "else:" nem kerül végrehajtásra!
print('\n** 4.n **')
for j in range(6):
    if j == 3: break
    print(f"j = {j}")
else:
    print(f"A ciklus végetért {i}")


print('\n** 5 **')
fruits = {"apple", "banana", "cherry"}.union({"carrot", "beetroot"})
# fruits = {"apple", "banana", "cherry"}.intersection({"carrot", "beetroot"})
for plant in fruits:
    print(plant)

print('\n** 6 **')
for element in [0, 1, 2]:
    pass
