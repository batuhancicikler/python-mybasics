# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:45:47 2019

@author: batuhan
"""

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
