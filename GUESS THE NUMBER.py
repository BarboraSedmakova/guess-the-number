#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:02:49 2023

@author: barbora
"""

import random
cislo = random.randint(1,100)
moj_odhad = input("Zadaj hodnotu! ")

while True:
    if moj_odhad == cislo:
       print("Uhádol si správne!")
    else:
        print("Neuhádol si správne!!")
        break
print(cislo)