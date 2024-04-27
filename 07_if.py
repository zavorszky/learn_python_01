# Project: 01
# File:    07_if.py
# Author:  zavorszky@yahoo.com

a = 200
b = 33
print(f"a = {a}, b =  {b}")
print("** 1 **")
if b > a:
    print("b > a")
elif a == b:
    print("b == a")
else:
    print("b < a")

# Az if rövidítése (tömör kódolása) - I.
print("\n")
print("** 2 **")
if a > b: print("Az (a) értéke nagyobb mint (b)-é.")

# Az if rövidítése (tömör kódolása) - II.
# Ezt nevezik "Ternary Operators"-nak (3x-os kifejezés) vagy
# "Conditional Expressions"-nek (feltételes kifejezés).
print("\n")
print("** 3 **")
print("a > b") if a > b else print("a <= b")

print("\n")
print("** 4 **")
print("a > b") if a > b else print("a == b") if a == b else print("a < b")

# Egymásba ágyazott if
print("\n")
print("** 4 **")
print(f"a = {a}")
if a > 10:
    print("a > 10")
    if a > 100:
        print("a > 100")
    else:
        print("a <= 100")

# Au üres utasítás, a semmit sem csinálás.
print("\n")
print("** 5 **")
if a < 10:
    pass
else:
    print("a >= b")