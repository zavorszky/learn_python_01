# Project: 01
# File: 15_dates.py
# Author: zavorszky@yahoo.com

print("** 1 **")
import datetime

now = datetime.datetime.now()
print(f"Aktuális dátum: {now}")

print("\n** 2 **")
print(now.year)
print(now.strftime("%A"))
print(now.strftime("%B"))
print(now.strftime("%Y-%m-%d %X"))

print("\n** 3 **")
dt = datetime.datetime(1958, 11, 27)
print(dt)
