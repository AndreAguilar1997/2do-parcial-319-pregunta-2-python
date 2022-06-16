# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 02:37:57 2022

@author: USER
"""
from functools import reduce

seriefibonaci = lambda n: reduce (lambda a, _: a + [a[-1] + a[-2]], range(n-2),[0,1])
nn=int(input("ingresar un numero "))
valor = seriefibonaci(nn)
print(valor)