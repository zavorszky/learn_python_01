# Project: 01
# File: 19_try.py
# Author: zavorszky@yahoo.com

print("** 1 **")
try:
    print(x)
except NameError:
    print("Hiba: Az 'x' változó nem definiált!")
except:
    print("Hiba: Egyéb hiba!")


print("\n** 2 **")
try:
    print("Hello!")
except:
    print('Hiba történt a "try" blokk végrehajása közben.')
else:
    print('Sikeres volt a "try" blokk végrehajása.')
finally:
    print('A "try" blokk után mindenképpen végrehajtásra kerül a "finally" blokk.')


print("\n** 3 **")
fname = "19_try.txt"
try:
    f=open(fname)
    try:
        f.write("Lorem Ipsum...")
    except:
        print(f"Hiba: Nem sikerült a {fname} file-ba írni.")
    finally:
        f.close()
except:
    print(f"Hiba: Nem sikerült az {fname} file-t megnyitni.")

# Figyelem!
# Ha kivétel történik (és nem kapjuk el), akkor a végrehajtás megszakad.

"""
print("\n** 4 **")
x = -1
if x < 0:
    raise Exception("Hiba: x nem lehet kisebb mint 0.")
"""

print("\n** 5 **")
x2 = 'Hello!'
if not type(x2) is int:
    raise TypeError("Hiba: x2 csak egész szám lehet.")
