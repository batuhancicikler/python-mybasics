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

#%% newton method

def root(n):
    roots = n/2
    for k in range(20):
        roots = (1/2) * (roots + (n/roots))
    return roots

#%%

liste = [1,2,3,4]
def yapya(liste):
    strs = ""
    for i in liste:
        a = str(i)
        strs = strs + a
    return strs

#%%

def obeb(a, b):
        while a%b != 0:
            olda = a
            oldb = b
            
            a = oldb
            b = olda % oldb
        return b

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):                              #print için method
        return str(self.num)+"/"+str(self.den)
        
    def show(self):
        print(self.num, "/", self.den)              #print harici göstermek için. artık gereksiz
    
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
    
    def __add__(self, other):                       # Toplama
        yeninum = self.num * other.den + self.den * other.num
        yeniden = self.den * other.den
        
        lowest = obeb(yeninum, yeniden)
        
        return Fraction(yeninum//lowest, yeniden//lowest)
    
    def __sub__(self, other):                       #çıkartma
        yeninum = self.num * other.den - self.den * other.num
        yeniden = self.den * other.den
        
        lowest = obeb(yeninum, yeniden)
        
        return Fraction(yeninum//lowest, yeniden//lowest)
    
    def __mul__(self, other):                       #çarpma
        yeninum = self.num * other.num
        yeniden = self.den * other.den
        
        lowest = obeb(yeninum, yeniden)
        
        return Fraction(yeninum//lowest, yeniden//lowest)
    
    def __truediv__(self, other):
        yeninum = self.num * other.num
        yeniden = self.den * other.den
        
        lowest = obeb(yeninum, yeniden)
        
        return Fraction(yeninum//lowest, yeniden//lowest)
    
    def __eq__(self, other):                        #eşitlik
        first = self.num * other.den
        second = self.den * other.num
        return first == second
    
    def __lt__(self, other):   #last then
        first = self.num * other.den
        second = self.den * other.num
        return first < second
    
    def __gt__(self, other):   #greater then
        first = self.num * other.den
        second = self.den * other.num
        return first > second
    
        
def main():
    f = Fraction(1,2)
    g = Fraction(5,4)
    print (f, "'nın payı ; ", f.getNum())
    print (g, "'nın paydası ; ", g.getDen())
    h = f + g
    j = Fraction(3,6)
    print (f, "+", g, "=", h)
    print(f, "-", j, "=", f-j)
    print (g, "ve", f, "eşit mi ?", g == f)
    print (f, "ve", j, "eşit mi ?", f == j)
    print (f, "ve", j, "eşit değil mi ?", f != j)
    print (g, "*", j, "=", g * j)
    print (f, "/", h, "=", f / h)
    print (g, "büyük mü", j, "den", g > j)
    print (h, "küçük mü", j, "den", h < j)
    
main()

#%% 


    






















    