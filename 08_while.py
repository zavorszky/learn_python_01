# Project: 01
# File:    08_while.py
# Author:  zavorszky@yahoo.com

# A "while" ciklust ki lehet egészíteni egy "else:" utasítással,
# amihet tartozó utasítások akkor kerülnek végrehajtásra, a ciklusfeltétel hamis.
# Ha a"while" feltétel egyszer sem teljesül (pl. az induláskor i = 10)
# az "else:" ág akkor is végrehajtásra kerül.
i = 0
while i < 6:
    i += 1
    print(f"Ciklus mag, i = {i}")
else:
    print(f"Ciklus utáni lépés, i = {i}")

