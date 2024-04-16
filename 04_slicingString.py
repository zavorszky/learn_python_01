# Project: 01
# File:    04_slicingString.py
# Author:  zavorszky@yahoo.com
#
# Ha egy sztringől metszünk ki egy rész egy intervallum megadásával,
# akkor az intervallum elejét kijelölő indexhez tartozó karakter
# beleszámít az eredménybe, de a végét megadó index karaktere NEM.
# Tehát balról zárt, jobbról nyílt intervallumot adtunk meg.

str_1 = "0123456789abc"
print(str_1 + ' (' + str(len(str_1)) + ')')
print('[2:5] :' + str_1[2:5])
print('[3:5] :' + str_1[3:5])
print('[3:6] :' + str_1[3:6])
print('[3:9] :' + str_1[3:9])
print('')
print('[0:10] :' + str_1[0:10])
print('[0:12] :' + str_1[0:12])
print('[0:13] :' + str_1[0:13])
print('[0:26] :' + str_1[0:26])
print('[0:1958] :' + str_1[0:1958])
print('')
print('[-1:5] :' + str_1[-1:5])
print('[-2:5] :' + str_1[-2:5])
print('[-3:5] :' + str_1[-3:5])
print('[-8:5] :' + str_1[-8:5])
print('[-9:5] :' + str_1[-9:5])
print('[-10:5] :' + str_1[-10:5])
print('[-11:5] :' + str_1[-11:5])
print('[-13:5] :' + str_1[-13:5])
print('')
print('Hello, World!'[1:3])
print('Hello, World!'[-5:-2])



