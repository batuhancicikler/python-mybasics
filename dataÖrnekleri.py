# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 01:49:14 2019

@author: batuhan
"""

#%% gruplama

from math import ceil

def gruplama(liste, slices):
   return list(map(lambda x: liste[x * slices:x * slices + slices],list(range(0, ceil(len(liste) / 2)))))
    
#%% 
liste=[4,5,2,"a","",True,False,0,1]

def filtre(x):
    return list(filter(bool, liste))

#%% liste içinde aranan elemanın sayısı
def saydır(liste, val):
    return len([i for i in liste if i == val and type(i) == type(val)])
#%% asal sayı kontrol --- 
    
def asalbul(x):
    for i in range(2, x):
        if x % i == 0:
            print("%d sayısı asal değildir\n"%(x), i, "*", x//i)
            break
        else:
            print("%d sayısı asaldır"%(x))
            break
        
#%% ** ile dict elemanlarını kwargs olarak kullanabilirsin.
            
def writing(a, b=5, vintage="blabla"):
    print("%s a ve %d b ve %s vintage"%(a,b,vintage))
    
d = {"a":5,"b":10, "vintage":"NOTblabla"}
writing(**d)










    