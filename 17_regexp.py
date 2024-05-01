# Project: 01
# File: 17_regexp.py
# Author: zavorszky@yahoo.com

import re

txt = "The rain in Spain"
print(txt)

reResultFindall = re.findall("ai", txt)
print("\n** reResultFindall **")
print(reResultFindall)

reResultSearch = re.search("ai", txt)
print("\n** reResultSearch **")
print(reResultSearch)

reResultSplit = re.split("\s", txt)
print("\n** reResultSplit **")
print(reResultSplit)

reResultSub = re.sub("\s", ":", txt)
print("\n** reResultSub **")
print(reResultSub)

print("\n** re.search(), start() **")
print(f"Szöveg: {txt}")
reResultSearch2 = re.search("\s", txt)
print(f"Az első elválasztó karakter pozíciója: {reResultSearch2.start()}")

print("\n** re.split(), a daradolás szabályozása... **")
print(f"Szöveg: {txt}")
reResultSplit21 = re.split("\s", txt, 1)
reResultSplit22 = re.split("\s", txt, 2)
print(reResultSplit21)
print(reResultSplit22)

print("\n** re.split(), a daradolás szabályozása... **")
print(f"Szöveg: {txt}")
reResultSub21 = re.sub("\s", ":", txt, 1)
reResultSub22 = re.sub("\s", ":", txt, 2)
print(reResultSub21)
print(reResultSub22)

print("\n** re.search(), span(), string(), group() **")
print(f"Szöveg: {txt}")
reResultSearch3 = re.search(r"\bS\w+", txt)
"""
Olyan egyezést ad vissza, ahol a megadott karakterek a szó elején vagy végén vannak.
(Az „r” az elején biztosítja, hogy a karakterlánc „nyers karakterláncként” legyen kezelve.)
(A puszta szövegkonstans nwm kerül értelmezésre/futtatásra.)
"""
# A .span() a találat kezdő- és végpozícióit tartalmazó sorral tér vissza.
print(reResultSearch3.span())

# A .string a függvénybe átadott karakterláncot adja vissza.
print(reResultSearch3.string)

# A .group() a karakterláncnak azt a részét adja vissza, ahol egyezés volt.
print(reResultSearch3.group())
