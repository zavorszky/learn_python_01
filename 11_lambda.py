# Project: 01
# File:    10_lambda.py
# Author:  zavorszky@yahoo.com

# Nekem úgy tűnik ez egy olyan lehetőség, mint a JavaScript-be az,
# hogy egy változóhoz rendelünk egy függvényt, vagy inkbb egy kifejezést.
print("** 1 **")
f = lambda a, b: a * b
print(f(5, 6))

print("\n** 2 **")


def myfunc(n):
    return lambda a: a * n


# A "mydoubler" a myfunction()-ból kap egy lambda függvényt ahol n=2.
# lambda a: a * 2
mydoubler = myfunc(2)

# A mydouber kiérteékeli a lambda kifejezést úgy hogy a=11.
# 11 * 2
value = mydoubler(11)
print(f"11 duplája = {value}")

print("\n** 3 **")
mytripler = myfunc(3)
value3 = mytripler(11)

print(f"11 triplája = {value3}")
