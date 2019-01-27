# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:31:39 2019

@author: batuhan
"""
#%%
import random

def gen(uzunluk):
    alfabe = "abcçdefghıijklmnoöprsştuüvyz "
    per = ""
    for i in range(uzunluk):
        per = per + alfabe[random.randrange(29)]
    return per

def skor(hedef, test):
    aynı = 0
    for i in range(len(hedef)):
        if hedef[i] == test[i]:
            aynı = aynı + 1
    return aynı / len(hedef)

def main():
    hedefstr = "batuhan"
    yenistr = gen(50)
    skorr2 = 0
    bestskor = skor(hedefstr, yenistr)
    while bestskor < 1:
        if bestskor >= skorr2:
            print (bestskor, yenistr)
            skorr2 = bestskor
        yenistr = gen(50)
        bestskor = skor(hedefstr, yenistr)
        
main()