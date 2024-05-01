# Project: 01
# File: 18_pip.py
# Author: zavorszky@yahoo.com

#
# PIP - Python package (module) menedzser.
# HA a verzió >= 3.4 AKKOR a PIP a Python-nal együtt van.
# EGYÉBKÉNT telepíteni kell.
#
# Telepítés forrása: https://pypi.org/project/pip/
#
# Python verzió ellenőrzése:
# > python --version
#
# PIP verzió ellenőrzése:
# > pip --version
#
# Egy package leöltése a PIP package "könyvtárából":
# > pip install <package_név>
#
# Pl.:
#  > pip install camelcase
#  stdout:
#  Collecting camelcase
#   Downloading camelcase-0.2.tar.gz (1.3 kB)
#   Installing build dependencies ... done
#   Getting requirements to build wheel ... done
#   Installing backend dependencies ... done
#   Preparing metadata (pyproject.toml) ... done
# Building wheels for collected packages: camelcase
#   Building wheel for camelcase (pyproject.toml) ... done
#   Created wheel for camelcase: filename=camelcase-0.2-py3-none-any.whl size=1778 sha256=7554e7f72fda693fe02acd0118b4a6c143022be85f88606cb93c60796cfd3e6c
#   Stored in directory: c:\users\dady\appdata\local\pip\cache\wheels\a7\40\a3\900133dd6de3e10c219659fec4118138db05d778e519c0b2bc
# Successfully built camelcase
# Installing collected packages: camelcase
# Successfully installed camelcase
#

#
# Uninstall package:
# > pip uninstall <package_név>
#
# List package
# > pip list
# stdout:
# Package   Version
# --------- -------
# camelcase 0.2
# pip       24.0
#
# Package-ek keresése:
# https://pypi.org/


# A "camelcase" package installálása.

# Importálni kell a package-t.
import camelcase

# A package tartalma használható.
cc = camelcase.CamelCase()

txt = "hello world!"

print(txt)
print(cc.hump(txt))
