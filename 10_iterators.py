# Project: 01
# File:    10_iterators.py
# Author:  zavorszky@yahoo.com

print('** 1 **')
# Ha "túl lépek" (next()) az utolsó elemen, akkor hiba esemény történik.
fruits_tuple = ("apple", "banana", "chery")
fruits_iter = iter(fruits_tuple)

print(next(fruits_iter))
print(next(fruits_iter))
print(next(fruits_iter))
# print(next(fruits_iter))

print('\n** 2 **')
fruit_string = "banana"
fruit_string_iter = iter(fruit_string)

print(next(fruit_string_iter))
print(next(fruit_string_iter))
print(next(fruit_string_iter))

print('\n** 3.a **')
# Készítsünk iterátor osztályt!
# __iret__ : kötelező függveény, visszaadja az iterátor objektumot (entitást?).
# __next__ : kötelező függvény, visszaadja a sorozat következő elemét.
class MyNumbers:
    def __iter__(self):
        self.i = 1
        return self
    
    def __next__(self):
        j = self.i
        self.i += 1
        return j

# Használjuk...
myLuckyNumbers_entity = MyNumbers()
myLuckyMumbers_iter = iter(myLuckyNumbers_entity)

print(next(myLuckyMumbers_iter))
print(next(myLuckyMumbers_iter))
print(next(myLuckyMumbers_iter))

print('\n** 3.b **')
class MyNumbers2:
    def __iter__(self):
        self.i = 1
        return self
    
    def __next__(self):
        if self.i <= 3:
            j = self.i
            self.i += 1
            return j
        else:
            raise StopIteration

myLuckyNumbers2_entity = MyNumbers2()
myLuckyMumbers2_iter = iter(myLuckyNumbers2_entity)

# A "for" leáll, a bekövetkezik a "StopIteration" kivétel.
# A kivételt nem kell elkapni.
for k in myLuckyMumbers2_iter:
    print(f"k = {k}")