# Project: 01
# File:    13_inheritance.py
# Author:  zavorszky@yahoo.com

print("** 1 **")


class Person:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(f"{self.lname} {self.fname}")


class Student(Person):
    pass


p = Person("István", "Závorszky")
s = Student("Dániel", "Závorszky")
p.printName()
s.printName()

# A gyerek objektum "__init__()"-e felülírja a szülő "__init__()"-ét.
# A "super()" a szülőre hivatkozik.
print("\n** 2 **")


class Person2:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(f"{self.lname} {self.fname}")


class Student2(Person2):
    def __init__(self, fname, lname) -> None:
        super().__init__(fname.upper(), lname.upper())


p2 = Person2("Anna", "Kovács")
s2 = Student2("Lilla", "Kovács")
p2.printName()
s2.printName()

print("\n** 3 **")


class Person3:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(f"{self.lname} {self.fname}")


class Student3(Person3):
    def __init__(self, fname, lname, gradYear) -> None:
        super().__init__(fname.upper(), lname.upper())
        self.gradYear = gradYear


s3 = Student3("Lőrinc", "Závorszky", 2005)
s3.printName()
print(f"Érettségi éve: {s3.gradYear}")

print("\n** 4 **")


class Person4:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(f"{self.lname} {self.fname}")


class Student4(Person4):
    def __init__(self, fname, lname, yearOfBirth) -> None:
        super().__init__(fname.upper(), lname.upper())
        self.yearOfBirth = yearOfBirth

    def graduationYear(self):
        return self.yearOfBirth + 18


s4 = Student4("Lőrinc", "Závorszky", 1987)
s4.printName()
print(f"Érettségi éve: {s4.graduationYear()}")
